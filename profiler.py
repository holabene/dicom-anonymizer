import time
import logging

logger = logging.getLogger(__name__)


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Execution time for {func.__name__}: {(end_time - start_time):.2f} seconds")
        return result

    return wrapper
