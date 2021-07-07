from server.config import db
from tag.models import Tag
from sqlalchemy.orm import relationship


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rep_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    country = relationship("CompanyCountry")

    def __init__(self, rep_name):
        self.rep_name = rep_name

    def __repr__(self):
        return self.rep_name


class CompanyCountry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    name = db.Column(db.String(100))
    country_type = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, company_id, name, country_type):
        self.company_id = company_id
        self.name = name
        self.country_type = country_type

    def __repr__(self):
        return f"{self.name}, {self.country_type}"


class CompanyTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

    def __repr__(self):
        return f"회사: {self.company_id}, tag:{self.tag_id}"
