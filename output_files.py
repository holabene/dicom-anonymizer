import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def disk_writer(output_dir: str):
    """
    Create a writer that writes to disk
    :param output_dir: Path to the output directory
    """
    def writer(bytes_iterator, path: str):
        # create directories if necessary
        os.makedirs(os.path.join(output_dir, os.path.dirname(path)), exist_ok=True)

        # write bytes_iterator to file
        with open(os.path.join(output_dir, path), 'wb') as file:
            while chunk := bytes_iterator.read(8192):
                file.write(chunk)

    return writer
