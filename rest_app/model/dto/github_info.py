from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class GithubData:
    commit_url: str
    commit_message: str
    commit_timestamp: str
    commit_github_author_username: str = ''


class GithubDataSchema(Schema):
    commit_url = fields.Str(data_key='url')
    commit_message = fields.Str(data_key='message')
    commit_timestamp = fields.Str(data_key='timestamp')

    @post_load
    def create_object(self, data, **kwargs):
        return GithubData(**data)
