import datetime
from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class UserRatingDto:
    user_id: str
    tests_passed: int
    tests_failed: int
    tests_count: int
    rating: float
    rating_max: int
    commit_url: str
    commit_message: str
    # commit_timestamp: any
    commit_github_author_username: str


class UserRatingDtoSchema(Schema):
    user_id = fields.Str(required=False)
    tests_passed = fields.Number()
    tests_failed = fields.Number()
    tests_count = fields.Number()
    rating = fields.Number()
    rating_max = fields.Number()
    commit_url = fields.Str()
    commit_message = fields.Str()
    # commit_timestamp = fields.DateTime(format='%Y-%m-%dT%H:%M:%S+02:00')
    commit_github_author_username = fields.Str()

    @post_load
    def create_object(self, data, **kwargs):
        return UserRatingDto(**data)
