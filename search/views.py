from flask import request
from flask_restx import Resource, Api, Namespace, fields
from search.selectors import get_company_names, get_tag_id, get_companys, get_tags, get_country_tags, get_company_name
from search.schema import search_companys_schema, search_tags_schema
from flask import jsonify
import json
from flask import Response


Search_API = Namespace(
    name="Search",
    description="Search(탐색) 관련 API.",
)


# 회사명 일부로 검색
@Search_API.route('')
@Search_API.doc(search={'search company name': 'tipped company name'})
class SearchCompany(Resource):
    @Search_API.response(200, 'Success')
    @Search_API.response(500, 'Failed')
    def get(self):
        """회사 검색을 통해 이름을 포함하는 회사를 찾습니다."""
        query = request.args.get('query')
        if not query:
            return {"msg": "검색어를 입력해 주세요"}, 400

        company_names = get_company_names(query)
        return search_companys_schema.jsonify(company_names)


# 태그로 검색
@Search_API.route('/company')
@Search_API.doc(params={'company_tag': 'company_tag'})
class Search(Resource):
    @Search_API.response(200, 'Success')
    @Search_API.response(500, 'Failed')
    def get(self):
        """태그를 통해 검색된 회사들의 정보를 가져옵니다"""
        company_tag = request.args.get('company_tag')
        if not company_tag:
            return {"msg": "태그를 입력해 주세요."}, 400

        # 태그 아이디 가져오기
        tag_id = get_tag_id(company_tag)
        if not tag_id:
            return {"msg": "태그에 맞는 회사가 존재하지 않습니다"}, 404

        # 태그를 가진 회사들의 아이디 가져오기
        companys = get_companys(tag_id)

        results = []
        # 회사별 태그 데이터셋으로 만들어서 전달하기
        for company in companys:
            data_set = {}
            tags = get_tags(company)
            all_tags = get_country_tags(tags)
            company_name = get_company_name(company.company_id)
            tags_set = []
            for tag in all_tags:
                tag_set = {}
                tag_set['tag_id'] = tag.tag_id
                tag_set['name'] = tag.name
                tags_set.append(tag_set)

            data_set['tags'] = tags_set
            data_set['id'] = company.company_id
            data_set['name'] = company_name
            results.append(data_set)

        return jsonify(results)
