from typing import List, Optional

from marshmallow import EXCLUDE

from common.configuration.logging import get_logger
from rest_app.model.dto.github_info import GithubDataSchema, GithubData
from rest_app.model.dto.test_suite import TestSuiteSchema, TestSuite, TestCaseSchema, TestCase

logger = get_logger(__name__)


def extract_component_test_results(data: dict) -> Optional[TestSuite]:
    try:
        test_suite_data = data['data']['data']['testsuite']['$']
        test_suite_schema = TestSuiteSchema()
        test_suite: TestSuite = test_suite_schema.load(test_suite_data)

        test_cases_data = [d['$'] for d in data['data']['data']['testsuite']['_']['testcase']]
        test_cases_schema = TestCaseSchema(many=True)
        test_cases: List[TestCase] = test_cases_schema.load(test_cases_data)

        test_suite.test_cases = test_cases

        return test_suite
    except KeyError as e:
        logger.error(e)
        return None


def extract_github_info(data: dict) -> Optional[GithubData]:
    try:
        head_commit = data['data']['head_commit']
        github_data: GithubData = GithubDataSchema().load(head_commit, unknown=EXCLUDE)
        github_data.commit_github_author_username = head_commit['author']['username']
        return github_data
    except KeyError as e:
        logger.error(e)
        return None
