# dicom_anonymizer/anonymizer.py

import os
import zipfile
import pydicom
import logging
import shutil

from pydicom.uid import generate_uid
from concurrent.futures import ThreadPoolExecutor

# configure log to stdout with basic formatting
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def get_new_uid(original_uid, uid_mapping):
    # Check if the original UID is already in the mapping
    existing_uid = uid_mapping.get(original_uid)
    if existing_uid:
        return existing_uid
    else:
        # Generate a new UID
        new_uid = generate_uid()
        # Store the mapping for future use
        uid_mapping[original_uid] = new_uid

        # Log the mapping
        logger.debug(f"New UID mapping: {original_uid} -> {new_uid}")

        return new_uid


def build_uid_mapping(input_file, uid_mapping):
    # Load the DICOM file
    ds = pydicom.dcmread(fp=input_file, stop_before_pixels=True, force=True,
                         specific_tags=['StudyInstanceUID', 'SeriesInstanceUID', 'SOPInstanceUID'])

    # Set the UIDs using the create_or_get_uid function
    get_new_uid(ds.StudyInstanceUID, uid_mapping)
    get_new_uid(ds.SeriesInstanceUID, uid_mapping)
    get_new_uid(ds.SOPInstanceUID, uid_mapping)


def update_uid_references(ds, uid_mapping):
    for data_element in ds:
        # Check if the data element is a sequence
        if data_element.VR == "SQ":
            # Recursively update UIDs in sequences
            for seq_item in data_element.value:
                update_uid_references(seq_item, uid_mapping)

        elif data_element.VR == "UI":
            # Find the value in the UID mapping
            value = data_element.value.decode('ascii') if isinstance(data_element.value, bytes) else data_element.value
            new_uid = uid_mapping.get(value)

            if new_uid:
                data_element.value = new_uid

                # Log tag, name and value as string
                logger.debug(f"Updated {data_element.tag} {data_element.name} {value} -> {new_uid}")
            else:
                # Log tag, name and value as string
                logger.debug(f"Not updating {data_element.tag} {data_element.name} {value}")


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


def anonymize_dicom_study(zip_file_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create random working directory to unzip the DICOM study
    working_dir = os.path.join(output_dir, f"tmp-{generate_uid()}")

    # Unzip the DICOM study
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(working_dir)

    # Determine the number of CPU cores
    num_cores = os.cpu_count()
    logger.debug(f"Number of CPU cores: {num_cores}")

    # First pass: Build the UID mapping without saving output files
    uid_mapping = {}

    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = []
        for root, dirs, files in os.walk(working_dir):
            for file in files:
                input_file_path = os.path.join(root, file)
                futures.append(executor.submit(build_uid_mapping, input_file_path, uid_mapping))

        # Wait for all tasks to complete
        for future in futures:
            future.result()

    # Second pass: Anonymize each DICOM file in the study by updating UID references
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = []
        for root, dirs, files in os.walk(working_dir):
            for file in files:
                input_file_path = os.path.join(root, file)
                futures.append(executor.submit(anonymize_dicom_file, input_file_path, output_dir, uid_mapping))

        # Wait for all tasks to complete
        for future in futures:
            future.result()

    # Delete the working directory
    shutil.rmtree(working_dir)
