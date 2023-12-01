import os
import logging
import zipfile

logger = logging.getLogger(__name__)


def iterate_files_in_directory(path):
    """
    Iterate over files in a directory
    :param path: Path to the directory
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            yield from iterate_files(os.path.join(root, file))


def iterate_files_in_zipfile(path):
    """
    Iterate over files in a zip file
    :param path: Path to the zip file
    """
    with zipfile.ZipFile(path) as zip_ref:
        for file in zip_ref.namelist():
            # Skip directories and dot files
            if file.endswith('/') or file.startswith('.'):
                continue

            # Skip Mac OS X metadata
            if '__MACOSX' in file or '.DS_Store' in file or '._' in file or '__Icon_' in file or '__' in file:
                continue

            logger.debug(f"Reading file {file} from zip file {path}")

            yield zip_ref.open(file)


def iterate_files(path):
    """
    Iterate over source files
    :param path: Path to the source files
    """
    # for directory
    if os.path.isdir(path):
        yield from iterate_files_in_directory(path)
    # for zip file
    elif zipfile.is_zipfile(path):
        yield from iterate_files_in_zipfile(path)
    # for file
    elif os.path.isfile(path):
        logger.debug(f"Reading file {path}")

        yield open(path, 'rb')
