import os
import logging
import httpx
import asyncio
import aioboto3

logger = logging.getLogger(__name__)


def disk_writer(output_dir: str):
    """
    Create a writer that writes to disk
    :param output_dir: Path to the output directory
    """
    def writer(file_object, path: str):
        # create directories if necessary
        os.makedirs(os.path.join(output_dir, os.path.dirname(path)), exist_ok=True)

        # write bytes_iterator to file
        with open(os.path.join(output_dir, path), 'wb') as file:
            while chunk := file_object.read(8192):
                file.write(chunk)

    return writer


def http_writer(url: str):
    """
    Create a writer that post to HTTP
    :param url: URL of the HTTP endpoint
    """
    async def async_http_writer(file_object, path: str):
        # create async iterator
        async def async_iterator():
            while chunk := file_object.read(8192):
                yield chunk

        content_type = 'application/zip' if path.endswith('.zip') else 'application/dicom'

        async with httpx.AsyncClient() as client:
            await client.post(url, data=async_iterator(), headers={'Content-Type': content_type})

    def writer(file_object, path: str):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_http_writer(file_object, path))

    return writer


def s3_writer(bucket: str, output_dir: str):
    """
    Create a writer that uploads to S3
    :param bucket: Name of the S3 bucket
    :param output_dir: Path to the output directory
    """
    session = aioboto3.Session()

    async def async_s3_writer(file_object, path: str):
        # create async iterator
        async with session.client('s3') as s3:
            await s3.upload_fileobj(Fileobj=file_object, Bucket=bucket, Key=f"{output_dir}/{path}")

    def writer(file_object, path: str):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_s3_writer(file_object, path))

    return writer
