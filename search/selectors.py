from company.models import CompanyCountry, Company, CompanyTag
from server.config import db
from tag.models import TagCountry


def get_company_names(query):
    company_names = db.session.query(CompanyCountry).filter(
        CompanyCountry.name.ilike(f"%{query}%")).all()
    return company_names


def get_tag_id(company_tag):
    tag = db.session.query(TagCountry).filter_by(
        name=company_tag).first()
    if tag:
        return tag.tag_id

    return tag


def get_tags(company):
    tags_id = db.session.query(CompanyTag).filter_by(
        company_id=company.company_id).all()
    return tags_id


def get_country_tags(tags):
    all_tags = db.session.query(TagCountry).filter(
        TagCountry.tag_id.in_([tag.tag_id for tag in tags])).filter_by(country_type="ko").all()
    return all_tags


def get_companys(tag_id):
    compayns_id = db.session.query(CompanyTag).filter_by(
        tag_id=tag_id).all()
    return compayns_id


def get_company_name(company_id):
    company = Company.query.get(company_id)
    return company.rep_name
