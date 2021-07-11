from flask import Blueprint, jsonify, Response

from common.decorators import inject_query_params
from common.utils.logging_utils import get_logger

rest_app = Blueprint('rest_app', __name__)

logger = get_logger(__name__)


@rest_app.post('/rate')
@inject_query_params(default_values={
    'payload': {'default_value': '', 'type': str}
})
def create_module_rating(payload: str, **kwargs) -> Response:
    logger.info(f'got payload:{payload}')
    return jsonify({'data': payload})
