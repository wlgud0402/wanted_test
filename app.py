from tag.models import *
from company.models import *
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api
from tag.views import Tag_API
from search.views import Search_API
from tag.models import Tag, TagCountry
from company.views import Company_API
from company.models import Company, CompanyCountry
from server.config import app, db, ma
import os

api = Api(
    app,
    version='0.1',
    title="김지형-원티드랩 API명세서",
    description="API경로, 파라미터, query등을 확인할 수 있는 API명세서 입니다.",
    terms_url="/",
    contact="jihyung.kim.dev@gmail.com",
    license="kim_jihyung"
)

api.add_namespace(Tag_API, '/api/tag')
api.add_namespace(Company_API, '/api/company')
api.add_namespace(Search_API, '/api/search')


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# Create a Product
@app.route("/product", methods=["POST"])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get All Products
@app.route("/product", methods=["GET"])
def get_products():
    all_products = Product.query.all()
    return products_schema.jsonify(all_products)

# GET Single Product


@app.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)


# Update a Product
@app.route("/product/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)


# Delete a Product
@app.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)


# db.init_app(app)
# db.app = app
# db.create_all()

# Run Server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
