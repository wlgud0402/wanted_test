from flask import request
from flask_restx import Resource, Api, Namespace, fields

Tag_API = Namespace(
    name="Tag",
    description="Tag 관련 API.",
)


@Tag_API.route('')
@Tag_API.doc(params={'todo_id': 'An ID'})
class Tag(Resource):
    @Tag_API.response(200, 'Success')
    @Tag_API.response(500, 'Failed')
    def get(self):
        """Tag에 관련된 API를 수행합니다.."""
        return {
            'tag': 1,
            'data': 1
        }
