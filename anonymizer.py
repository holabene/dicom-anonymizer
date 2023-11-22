# dicom_anonymizer/anonymizer.py

import os
import zipfile
import pydicom
import logging
import shutil

from pydicom.uid import generate_uid
from concurrent.futures import ThreadPoolExecutor

from uid import build_uid_mapping, update_uid_references
from profiler import measure_time
from input_files import iterate_files

# configure log to stdout with basic formatting
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def anonymize_dicom_file(input_file, output_dir, uid_mapping):
    # Load the DICOM file
    ds = pydicom.dcmread(fp=input_file, stop_before_pixels=True, force=True)

    # Anonymize the DICOM file
    # Replace or remove identifiable information
    ds.PatientName = "Anonymous"
    ds.PatientID = "AnonID"

    update_uid_references(ds, uid_mapping)

    # Save the anonymized DICOM file to path StudyInstanceUID/SeriesInstanceUID/SOPInstanceUID.dcm
    # Create directories if necessary
    output_path = os.path.join(output_dir, ds.StudyInstanceUID, ds.SeriesInstanceUID)
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, ds.SOPInstanceUID + ".dcm")
    ds.save_as(output_file, write_like_original=False)


@measure_time
def anonymize_dicom_study(source_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Determine the number of CPU cores
    num_cores = os.cpu_count()
    logger.debug(f"Number of CPU cores: {num_cores}")

    # First pass: Build the UID mapping without saving output files
    uid_mapping = build_uid_mapping(source_path)

    # Second pass: Anonymize each DICOM file in the study by updating UID references
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = []
        for fp in iterate_files(source_path):
            futures.append(executor.submit(anonymize_dicom_file, fp, output_dir, uid_mapping))

        # Wait for all tasks to complete
        for future in futures:
            future.result()
