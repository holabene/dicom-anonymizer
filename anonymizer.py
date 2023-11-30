# dicom_anonymizer/anonymizer.py

import os
import pydicom
import logging
import io

from uid import build_uid_mapping, update_uid_references
from profiler import measure_time
from input_files import iterate_files
from output_files import disk_writer

from concurrent.futures import ThreadPoolExecutor
from stream_zip import ZIP_32, stream_zip
from stat import S_IFREG
from to_file_like_obj import to_file_like_obj
from datetime import datetime

# configure log to stdout with basic formatting
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
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
def anonymize_dicom_study(source_path, zip_output, **kwargs):
    # Build the UID mapping
    uid_mapping = build_uid_mapping(source_path)

    # Get --output-dir argument
    output_dir = kwargs.get('output_dir', '.')

    # Create writer
    writer = disk_writer(output_dir)

    # Anonymize each DICOM file in the study by updating UID references
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []
        for fp in iterate_files(source_path):
            futures.append(executor.submit(anonymize_dicom_file, fp, uid_mapping))

        # Wait for all tasks to complete
        def results():
            for future in futures:
                buffer, path = future.result()
                if zip_output:
                    yield path, datetime.now(), S_IFREG | 0o600, ZIP_32, (buffer.getvalue(),)
                else:
                    yield buffer, path

        # path is results_{timestamp}_{microsecond}
        output_name = f'output_{datetime.now().strftime("%Y%m%d_%H%M%S_%f")}'

        if zip_output:
            writer(to_file_like_obj(stream_zip(results())), f'{output_name}.zip')
            logger.info(f'Zip file {os.path.join(output_dir, output_name)}.zip created')
        else:
            for dicom_data, path_to_file in results():
                writer(to_file_like_obj(dicom_data), os.path.join(output_name, path_to_file))

            logger.info(f'DICOM files written to {os.path.join(output_dir, output_name)}')
