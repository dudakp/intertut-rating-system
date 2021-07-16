from dataclasses import dataclass, field

from typing import List

from marshmallow import Schema, fields, post_load


@dataclass
class TestCase:
    class_name: str
    name: str
    time: float


class TestCaseSchema(Schema):
    class_name = fields.Str(data_key='classname')
    name = fields.Str()
    time = fields.Number()

    @post_load
    def create_object(self, data, **kwargs):
        return TestCase(**data)


@dataclass
class TestSuite:
    errors: int
    failures: int
    name: str
    tests: int
    time: float
    test_cases: List[TestCase] = field(default_factory=list)


class TestSuiteSchema(Schema):
    errors = fields.Number()
    failures = fields.Number()
    name = fields.Str()
    tests = fields.Number()
    time = fields.Number()

    @post_load
    def create_object(self, data, **kwargs):
        return TestSuite(**data)
