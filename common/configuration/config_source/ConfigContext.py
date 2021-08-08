from pika import BlockingConnection

from common.configuration.ampq_config import setup_amqp_connection


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigContext(metaclass=SingletonMeta):
    """
    All things that should be shared across app (and produces some object) has to be initialized here
    """
    __slots__ = []  # all properties of class are read-only
    amqp_connection: BlockingConnection = setup_amqp_connection()
