from flask import request
from flask_restx import Resource, Api, Namespace, fields
from company.selectors import get_company, get_tag, have_tag
from company.services import company_tag_add, delete_company_tag

Company_API = Namespace(
    name="Company",
    description="Company 관련 API.",
)

company_tag_add_fields = Company_API.model('company_tag_add', {
    'company_id': fields.Integer,
    'tag_id': fields.Integer,
})


@Company_API.route('')
@Company_API.doc(params={'todo_id': 'An ID'})
class Company(Resource):
    @Company_API.response(200, 'Success')
    @Company_API.response(500, 'Failed')
    def get(self):
        """Company를 등록하거나 삭제하는 역할을 수행합니다."""
        return {
            'todo_id': 1,
            'data': 1
        }


@Company_API.route('/tag')
class CompanyTag(Resource):
    @Company_API.expect(company_tag_add_fields, validate=True)
    @Company_API.response(200, 'Success')
    @Company_API.response(500, 'Failed')
    def post(self):
        """회사에 태그 정보를 추가합니다."""
        company_id = request.json.get("company_id")
        tag_id = request.json.get("tag_id")

        company = get_company(company_id)
        tag = get_tag(tag_id)
        if not company:
            return {"msg": "존재하지 않는 회사입니다."}, 400

        if not tag:
            return {"msg": "존재하지 않는 태그입니다."}, 400

        is_have_tag = have_tag(company, tag)
        if not is_have_tag:
            company_tag_add(company, tag)
            return {"msg": "회사 태그 추가에 성공하였습니다"}, 201

        return {"msg": "이미 태그 되어 있습니다."}, 400


@Company_API.route('/<int:company_id>/tag/<int:tag_id>')
@Company_API.doc(params={'company,todo id ': 'company, todo id'})
class CompanyTagDelete(Resource):
    @Company_API.response(200, 'Success')
    @Company_API.response(500, 'Failed')
    def delete(self, company_id, tag_id):
        try:
            company_id = int(company_id)
            tag_id = int(tag_id)
            delete_company_tag(company_id, tag_id)
            return {"msg": "삭제가 완료되었습니다."}, 204
        except:
            return {"msg": "잘못된 회사/태그 아이디입니다."}, 400
