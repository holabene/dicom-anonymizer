import io
import os


def disk_writer(output_dir: str):
    """
    Create a writer that writes to disk
    :param output_dir: Path to the output directory
    """
    def writer(buffer: io.BytesIO, path: str):
        # create directories if necessary
        os.makedirs(os.path.join(output_dir, os.path.dirname(path)), exist_ok=True)

        # write buffer to disk
        buffer.seek(0)

        with open(os.path.join(output_dir, path), 'wb') as f:
            f.write(buffer.read())

    return writer
