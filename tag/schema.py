from server.config import ma


class TestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


# Init Schema
test_schema = TestSchema()
tests_schema = TestsSchema(many=True)
