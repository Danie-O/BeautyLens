from app import app, db, login, ma
from flask import jsonify
from flask_cors import CORS,cross_origin
from models import User, Product, products_schema, Recommendation, BlogPost, Comment
import random


@app.route('/', methods=['GET'])
def index():
    return "Hello, world!"

@app.route('/api/products', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'])
def get_all_products():
    all_products = Product.query.all()
    if not all_products:
        all_products = []

    all_products = products_schema.dump(all_products)
        
    return jsonify(all_products)

@app.route('/api/some_products', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'])
def get_some_products():
    all_products = Product.query.all()
    if not all_products:
        all_products = []

    all_products = products_schema.dump(all_products)

    unique_products = []
    seen_product_ids = set()
    seen_brand_names = set()

    random.shuffle(all_products)

    for product in all_products:
        if len(unique_products) == 6:
            break
        else:
            if product['id'] not in seen_product_ids and product['brand'] not in seen_brand_names:
                unique_products.append(product)
                seen_product_ids.add(product['id'])
                seen_brand_names.add(product['brand'])
    
    return jsonify(unique_products)


if __name__ == "__main__":
    app.run(debug=True)