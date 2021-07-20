from server.config import ma
from marshmallow import fields


class SearchCompanySchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    country_type = fields.Str()


class SearchTagSchema(ma.Schema):
    tag_id = fields.Int()
    name = fields.Str()


search_companys_schema = SearchCompanySchema(many=True)
search_tags_schema = SearchTagSchema(many=True)
