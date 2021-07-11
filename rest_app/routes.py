from flask import Blueprint, jsonify, Response

from common.decorators import inject_query_params

rest_app = Blueprint('rest_app', __name__)


@rest_app.post('/rate')
@inject_query_params(default_values={
    'payload': {'default_value': '', 'type': str}
})
def create_module_rating(payload: str, **kwargs) -> Response:
    return jsonify({'data': payload})
