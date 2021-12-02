# wsgi.py
# pylint: disable=missing-docstring

BASE_URL = '/api/v1'

from flask import Flask, jsonify
from config import DevelopmentConfig
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

from models import Product

from schemas import many_product_schema, one_product_schema

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['GET'])
def get_one_product(product_id):
    product = db.session.query(Product).get(product_id) # SQLAlchemy request => 'SELECT * FROM products'
    return one_product_schema.jsonify(product), 200



