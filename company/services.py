from company.models import CompanyTag
from server.config import db


def company_tag_add(company, tag):
    added_company_tag = CompanyTag(company_id=company.id, tag_id=tag.id)

    db.session.add(added_company_tag)
    db.session.commit()
    return added_company_tag


def delete_company_tag(company_id, tag_id):
    try:
        company_tag = CompanyTag.query.filter_by(
            company_id=company_id).filter_by(tag_id=tag_id).first()
        db.session.delete(company_tag)
        db.session.commit()
        return company_tag
    except:
        return False


def have_tag(company, tag):
    have_tag = None
    try:
        have_tag = CompanyTag.query.filter_by(
            company_id=company.id).filter_by(tag_id=tag.id).first()
    except:
        return have_tag
    return have_tag
