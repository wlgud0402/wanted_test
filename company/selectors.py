from company.models import Company, CompanyTag
from tag.models import Tag
from server.config import db


def get_company(company_id):
    company = Company.query.get(company_id)
    return company


def get_tag(tag_id):
    tag = Tag.query.get(tag_id)
    return tag


def have_tag(company, tag):
    have_tag = None
    try:
        have_tag = CompanyTag.query.filter_by(
            company_id=company.id).filter_by(tag_id=tag.id).first()
    except:
        return have_tag
    return have_tag
