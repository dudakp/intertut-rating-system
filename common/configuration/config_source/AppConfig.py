from os import environ
from typing import List

from dotenv import load_dotenv

load_dotenv()


class AppConfig:
    MONGO_URL: str = environ.get('MONGO_URL')
    RABBIT_URL: str = environ.get('RABBIT_URL')
    RABBIT_USER: str = environ.get('RABBIT_USER')
    RABBIT_PWD: str = environ.get('RABBIT_PWD')
    RABBIT_EXCHANGES: List[str] = environ.get('RABBIT_EXCHANGES').split(',')
    RABBIT_QUEUES: List[str] = environ.get('RABBIT_QUEUES').split(',')
    RABBIT_QUEUE_BINDINGS: List[str] = environ.get('RABBIT_QUEUE_BINDINGS').split(',')
