from server.config import ma
from marshmallow import fields


class SearchCompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'country_type')


class SearchTagSchema(ma.Schema):
    class Meta:
        fields = ('tag_id', 'name')


search_companys_schema = SearchCompanySchema(many=True)
search_tags_schema = SearchTagSchema(many=True)
