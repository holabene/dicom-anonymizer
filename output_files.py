import os
import logging
import httpx
import asyncio

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


def http_writer(url: str):
    """
    Create a writer that writes to HTTP
    :param url: URL of the HTTP endpoint
    """
    async def async_http_writer(bytes_iterator, path: str):
        # create async iterator
        async def async_iterator():
            while chunk := bytes_iterator.read(8192):
                yield chunk

        content_type = 'application/zip' if path.endswith('.zip') else 'application/dicom'

        async with httpx.AsyncClient() as client:
            await client.post(url, data=async_iterator(), headers={'Content-Type': content_type})

    def writer(bytes_iterator, path: str):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_http_writer(bytes_iterator, path))

    return writer
