import io
import os
import zipfile
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def zip_output(writer):
    """
    A decorator that adds zip functionality to a writer
    """
    zip_buffer = io.BytesIO()

    def wrapper(buffer: io.BytesIO, path: str):
        # get first part of path as zip file name
        zip_file_name = path.split('/')[0] + '.zip'

        logger.debug(f"Writing file {path} to zip file {zip_file_name}")

        # write buffer to zip buffer
        buffer.seek(0)

        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_ref:
            zip_ref.writestr(path, buffer.read())

        return writer(zip_buffer, zip_file_name)

    return wrapper


def disk_writer(output_dir: str):
    """
    Create a writer that writes to disk
    :param output_dir: Path to the output directory
    """

    @zip_output
    def writer(buffer: io.BytesIO, path: str):
        # create directories if necessary
        os.makedirs(os.path.join(output_dir, os.path.dirname(path)), exist_ok=True)

        # write buffer to disk
        buffer.seek(0)

        with open(os.path.join(output_dir, path), 'wb') as f:
            f.write(buffer.read())

    return writer
