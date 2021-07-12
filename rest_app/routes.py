import json

from flask import Blueprint, jsonify, Response, request

from common.decorators import inject_query_params
from common.utils.logging_utils import get_logger

rest_app = Blueprint('rest_app', __name__)

logger = get_logger(__name__)

# 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
@rest_app.post('/rate')
@inject_query_params(default_values={
    'payload': {'default_value': '', 'type': str}
})
def create_module_rating(payload: str, **kwargs) -> Response:
    logger.info(request.data)
    logger.info(f'got payload:{payload}')
    return jsonify({'data': json.loads(request.data)})
