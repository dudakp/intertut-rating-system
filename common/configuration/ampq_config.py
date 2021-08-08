import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel

from common.configuration.config_source.AppConfig import AppConfig
from common.configuration.logging import get_logger

logger = get_logger(__name__)


def setup_amqp_connection() -> BlockingConnection:
    logger.info(f'Connecting to amqp server with user: {AppConfig.RABBIT_USER}')
    credentials = pika.PlainCredentials(username=AppConfig.RABBIT_USER, password=AppConfig.RABBIT_PWD)
    parameters = pika.ConnectionParameters(host=AppConfig.RABBIT_URL, virtual_host=AppConfig.RABBIT_USER,
                                           credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    declare_queues(connection.channel())
    configure_exchanges(connection.channel())
    return connection


def declare_queues(channel: BlockingChannel) -> None:
    logger.info('Creating Rabbit queues')
    for queue in AppConfig.RABBIT_QUEUES:
        channel.queue_declare(queue=queue)
        logger.info(f'{queue=} created')
    logger.info('all rabbit queues created')


def configure_exchanges(channel: BlockingChannel) -> None:
    logger.info('Creating rabbit exchanges')
    for x in AppConfig.RABBIT_EXCHANGES:
        xcfg = x.split(':')
        channel.exchange_declare(exchange=xcfg[0],
                                 exchange_type=xcfg[1])
        logger.info(f'Created exchange: {x}')
    logger.info('Creating queues binding')
    for b in AppConfig.RABBIT_QUEUE_BINDINGS:
        bind = b.split(':')
        channel.queue_bind(bind[0], bind[1], bind[2])
        logger.info(f'Created binding: {b}')
