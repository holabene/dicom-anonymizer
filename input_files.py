import os
import logging
import zipfile

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
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
            # Skip directories and MACOSX files and dot files
            if file.endswith('/') or file.startswith('__MACOSX') or file.startswith('.'):
                continue

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
        yield open(path, 'rb')
