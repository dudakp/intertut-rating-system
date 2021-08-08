from typing import List, Tuple

import flask
from flask import Flask, Blueprint
from flask_cors import CORS

from common.configuration.datasource import connect_to_datasource
from common.configuration.logging import get_logger
from rest_app.routes import rest_app

logger = get_logger(__name__)


def create_app(name: str) -> flask.app:
    """
    Configurations that dont produce any objects should be configured here
    :param name: app name
    :return: flask app instance
    """
    app = Flask(name)
    connect_to_datasource()
    CORS(app)
    register_blueprints(app)
    logger.info('web_app initialization complete')
    return app


def register_blueprints(app_instance: flask.app) -> None:
    modules: List[Tuple[Blueprint, str]] = [(rest_app, '/rest-app')]
    for module in modules:
        try:
            logger.info(f'registering {module[1]}')
            app_instance.register_blueprint(module[0], url_prefix=module[1])
        except Exception as e:
            logger.warning(f'Failure in registering module {module[1]}, {e}')
