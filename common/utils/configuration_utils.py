from typing import List, Tuple

import flask
from flask import Flask, Blueprint
from flask_cors import CORS

from common.utils.logging_utils import get_logger
from rest_app.routes import rest_app

logger = get_logger(__name__)


def create_app(name: str) -> flask.app:
    app = Flask(name)
    CORS(app)
    register_blueprints(app)
    logger.info('web_app inicialization complete')
    return app


def register_blueprints(app_instance: flask.app) -> None:
    modules: List[Tuple[Blueprint, str]] = [(rest_app, '/rest-app')]
    for module in modules:
        try:
            logger.info(f'registering {module[1]}')
            app_instance.register_blueprint(module[0], url_prefix=module[1])
        except Exception as e:
            logger.warning(f'Failure in registering module {module[1]}, {e}')
