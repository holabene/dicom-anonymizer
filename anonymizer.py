# dicom_anonymizer/anonymizer.py

import os
import pydicom
import logging
import io

from uid import build_uid_mapping, update_uid_references
from profiler import measure_time
from input_files import iterate_files
from output_files import disk_writer, http_writer, s3_writer

from concurrent.futures import ThreadPoolExecutor
from stream_zip import ZIP_32, stream_zip
from stat import S_IFREG
from to_file_like_obj import to_file_like_obj
from datetime import datetime
from urllib.parse import urlunparse, urlparse

# configure log to stdout with basic formatting
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def anonymize_dicom_file(input_file, uid_mapping):
    # Load the DICOM file
    ds = pydicom.dcmread(fp=input_file, force=True)

    # Anonymize the DICOM file
    # Replace or remove identifiable information
    ds.PatientName = "Anonymous"
    ds.PatientID = "AnonID"

    update_uid_references(ds, uid_mapping)

    # Write the anonymized DICOM file to buffer
    path = f"{ds.StudyInstanceUID}/{ds.SeriesInstanceUID}/{ds.SOPInstanceUID}.dcm"
    buffer = io.BytesIO()
    ds.save_as(buffer, write_like_original=False)
    buffer.seek(0)

    return buffer, path


@measure_time
def anonymize_dicom_study(input_path, output_path, zip_output):
    # Build the UID mapping
    uid_mapping = build_uid_mapping(input_path)

    # Parse output path URL
    parts = urlparse(output_path)
    output_path = urlunparse((parts.scheme, parts.netloc, parts.path, parts.params, parts.query, parts.fragment))
    output_name = f'results_{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}' + ('.zip' if zip_output else '')

    # Create writer
    if parts.scheme == 'http' or parts.scheme == 'https':
        writer = http_writer(output_path)
        final_message = f'Results posted to {output_path}'
    elif parts.scheme == 's3':
        output_path = urlunparse(("s3", parts.netloc, parts.path.rstrip("/"), "", "", ""))
        writer = s3_writer(output_path)
        final_message = f'Results uploaded to {output_path}/{output_name}'
    elif parts.scheme == '':
        writer = disk_writer(parts.path)
        final_message = f'Results saved to {os.path.abspath(os.path.join(parts.path, output_name))}'
    else:
        raise ValueError(f'Unsupported output method: {parts.scheme}')

    # Anonymize each DICOM file in the study by updating UID references
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []
        for fp in iterate_files(input_path):
            futures.append(executor.submit(anonymize_dicom_file, fp, uid_mapping))

        # Wait for all tasks to complete
        def results():
            for future in futures:
                buffer, path = future.result()
                if zip_output:
                    yield path, datetime.now(), S_IFREG | 0o600, ZIP_32, (buffer.getvalue(),)
                else:
                    yield buffer, path

        if zip_output:
            writer(to_file_like_obj(stream_zip(results())), output_name)
        else:
            for dicom_data, path_to_file in results():
                writer(to_file_like_obj(dicom_data), os.path.join(output_name, path_to_file))

    logger.info(f"Finished processing {len(futures)} files from {os.path.abspath(input_path)}")
    logger.info(final_message)
