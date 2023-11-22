# dicom_anonymizer/anonymizer.py

import os
import pydicom
import logging
import io
from concurrent.futures import ThreadPoolExecutor

from uid import build_uid_mapping, update_uid_references
from profiler import measure_time
from input_files import iterate_files
from output_files import disk_writer

# configure log to stdout with basic formatting
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def anonymize_dicom_file(input_file, writer, uid_mapping):
    # Load the DICOM file
    ds = pydicom.dcmread(fp=input_file, stop_before_pixels=True, force=True)

    # Anonymize the DICOM file
    # Replace or remove identifiable information
    ds.PatientName = "Anonymous"
    ds.PatientID = "AnonID"

    update_uid_references(ds, uid_mapping)

    # Write the anonymized DICOM file to buffer
    path = f"{ds.StudyInstanceUID}/{ds.SeriesInstanceUID}/{ds.SOPInstanceUID}.dcm"
    buffer = io.BytesIO()
    ds.save_as(buffer, write_like_original=False)
    writer(buffer, path)


@measure_time
def anonymize_dicom_study(source_path, output_dir):
    # Build the UID mapping
    uid_mapping = build_uid_mapping(source_path)

    # Create writer
    writer = disk_writer(output_dir)

    # Anonymize each DICOM file in the study by updating UID references
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []
        for fp in iterate_files(source_path):
            futures.append(executor.submit(anonymize_dicom_file, fp, writer, uid_mapping))

        # Wait for all tasks to complete
        for future in futures:
            future.result()
