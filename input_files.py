import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def iterate_files(path):
    """
    Iterate over source files
    :param path: Path to the source files
    """
    # for directory
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                path = os.path.join(root, file)
                yield open(path, 'rb')
    # for file
    elif os.path.isfile(path):
        yield open(path, 'rb')
