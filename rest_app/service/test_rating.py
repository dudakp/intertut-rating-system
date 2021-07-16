from datetime import datetime

from marshmallow import EXCLUDE

from rest_app.model.db.UserRating import UserRating
from rest_app.model.dto.github_info import GithubData
from rest_app.model.dto.test_suite import TestSuite
from rest_app.model.rest.UserRatingDto import UserRatingDtoSchema, UserRatingDto


def rate_tests(testsuite: TestSuite, github_data: GithubData) -> UserRatingDto:
    saved_json = UserRating(user_id='user-123-',
                            tests_passed=testsuite.tests - testsuite.failures,
                            tests_failed=testsuite.failures,
                            tests_count=testsuite.tests,
                            rating=testsuite.tests - (testsuite.tests / (testsuite.tests - testsuite.failures)),
                            rating_max=1,
                            commit_url=github_data.commit_url,
                            commit_message=github_data.commit_message,
                            commit_timestamp=datetime.fromisoformat(github_data.commit_timestamp),
                            commit_github_author_username=github_data.commit_github_author_username) \
        .save().to_mongo()
    return UserRatingDtoSchema(unknown=EXCLUDE).load(saved_json)
