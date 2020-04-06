from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template

product_app = Blueprint('product_app', __name__)


PRODUCTS = {
    1: 'Phone',
    2: 'Tablet',
    3: 'Laptop',
}


@product_app.route('/', endpoint='products')
def index():
    return render_template('product/index.html', products=PRODUCTS.items())


@product_app.route('/<int:product_id>/', endpoint='product')
def get_product(product_id):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise NotFound(f'There is no product #{product_id}')
    return render_template(
        'product/product.html',
        product_id=product_id,
        product_name=product_name,
    )
