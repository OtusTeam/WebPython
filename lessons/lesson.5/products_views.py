from flask import Blueprint


products_app = Blueprint('products_app', __name__)


@products_app.route('/', endpoint='products')
def products_page():
    return '<h1>Products Page!</h1>'


@products_app.route('/<int:product_id>/', endpoint='product')
def product_page(product_id):
    return f'<h1>Product {product_id}</h1>'
