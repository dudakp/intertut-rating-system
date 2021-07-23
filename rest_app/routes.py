import json

from flask import Blueprint, jsonify, Response, request

from common.configuration.logging import get_logger
from rest_app.service.data_extraction import extract_component_test_results, extract_github_info
from rest_app.service.test_rating import rate_tests

rest_app = Blueprint('rest_app', __name__)

logger = get_logger(__name__)


@rest_app.post('/rate')
def create_module_rating() -> Response:
    logger.info('Started rating processing for user: ')
    data = request.data
    dict_data = json.loads(data)

    test_results = extract_component_test_results(dict_data)
    github_info = extract_github_info(dict_data)
    rating = rate_tests(test_results, github_info)
    return jsonify({'rating': rating})
