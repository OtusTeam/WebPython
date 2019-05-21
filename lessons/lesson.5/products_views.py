from werkzeug.exceptions import NotFound, abort
from flask import Blueprint, render_template

products_app = Blueprint('products_app', __name__)

PRODUCTS = {
    1: 'Laptop',
    2: 'Phone',
    3: 'Tablet',
}


@products_app.route('/', endpoint='products')
def products():
    return render_template('products/index.html', products=PRODUCTS.items())


# @products_app.route('/<int:id>/<float:price>/<name>')
@products_app.route('/<int:product_id>/', endpoint='product')
def product(product_id):
    # return f'<h1>Product #{product_id} {name!r} ${price}</h1>'
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        # abort(404)
        # return f'Product #{product_id} does not exist!', 404
        raise NotFound(f'Product #{product_id} does not exist!')
    return f'<h1>Product #{product_id} is {product_name}</h1>'
