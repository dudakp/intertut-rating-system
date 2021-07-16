from mongoengine import Document, StringField, ObjectIdField, IntField, FloatField, DateTimeField


class UserRating(Document):
    user_id = StringField()
    tests_passed = IntField()
    tests_failed = IntField()
    tests_count = IntField()
    rating = FloatField()
    rating_max = IntField()  # toto mozno normalizovat do separatnej kolekcie nieco ako test_data
    commit_url = StringField()  # data.head_commit.url
    commit_message = StringField()  # data.head_commit.message
    commit_timestamp = DateTimeField()  # data.head_commit.timestamp
    commit_github_author_username = StringField()  # data.head_commit.author.username
