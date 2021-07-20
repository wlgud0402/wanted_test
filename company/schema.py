from server.config import ma
from marshmallow import fields


class TestSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()


# Init Schema
test_schema = TestSchema()
tests_schema = TestsSchema(many=True)
