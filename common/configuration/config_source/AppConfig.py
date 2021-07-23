import os


class AppConfig:
    MONGO_URL = os.environ.get('MONGO_URL')
