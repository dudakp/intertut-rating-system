import logging
import sys

STREAM_LOGGER_FORMAT = '[%(levelname)s] - %(asctime)s - %(name)s:%(lineno)d - %(message)s'


def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_formatter = logging.Formatter(STREAM_LOGGER_FORMAT)
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)

    return logger
