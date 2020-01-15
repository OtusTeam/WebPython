from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template, abort

products_app = Blueprint('products_app', __name__)


PRODUCTS = {
    1: 'Phone',
    2: 'Tablet',
    3: 'Laptop',
}


@products_app.route('/', endpoint='products')
def products_list():
    return render_template(
        'products/index.html',
        products=PRODUCTS.items(),
    )


# @products_app.route('/<int:id>/')
# @products_app.route('/<float:price>/')
# @products_app.route('/<int:id>/<float:price>/')
# def product_info(id, price):
#     return f'<h2>Info about product #{id} ${price}</h2>'

@products_app.route('/<int:id>/', endpoint='product')
def product_info(id):
    try:
        product_name = PRODUCTS[id]
    except KeyError:
        # return 'eroro', 444
        raise NotFound(f'There is no product #{id}')
        # abort(418)

    return f'Product #{id}: {product_name}'
