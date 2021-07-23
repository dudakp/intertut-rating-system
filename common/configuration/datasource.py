from mongoengine import connect

from common.configuration.config_source.AppConfig import AppConfig
from common.configuration.logging import get_logger

logger = get_logger(__name__)


def connect_to_datasource() -> None:
    logger.info('Connecting to database')
    try:
        connect(
            host=AppConfig.MONGO_URL
        )
    except Exception as e:
        logger.info('Error connecting to database.', e)
    logger.info('Sucesfully connected to database')
