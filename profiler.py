import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.debug(f"Execution time for {func.__name__}: {(end_time - start_time):.2f} seconds")
        return result

    return wrapper
