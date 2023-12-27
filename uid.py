import logging
import os

import pydicom

from pydicom.uid import generate_uid
from concurrent.futures import ThreadPoolExecutor
from input_files import iterate_files

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


def get_new_uid_from_file(input_file, uid_mapping):
    # Load the DICOM file
    ds = pydicom.dcmread(fp=input_file, force=True,
                         specific_tags=['StudyInstanceUID', 'SeriesInstanceUID', 'SOPInstanceUID'])

    # Set the UIDs using the create_or_get_uid function
    get_new_uid(ds.StudyInstanceUID, uid_mapping)
    get_new_uid(ds.SeriesInstanceUID, uid_mapping)
    get_new_uid(ds.SOPInstanceUID, uid_mapping)


def build_uid_mapping(source):
    uid_mapping = {}
    files_count = None

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []
        for fp in iterate_files(source):
            futures.append(executor.submit(get_new_uid_from_file, fp, uid_mapping))

        # Wait for all tasks to complete
        for future in futures:
            future.result()

        files_count = len(futures)

    return uid_mapping, files_count


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
