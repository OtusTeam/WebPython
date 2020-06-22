from flask import Blueprint, render_template
from werkzeug.exceptions import BadRequest

products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Phone",
    2: "Tablet",
    3: "Laptop",
}


@products_app.route("/", endpoint="products")
def products_list():
    return render_template("products/index.html", products=PRODUCTS.items())


@products_app.route("/<int:product_id>/", endpoint="product")
def product_detail(product_id):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise BadRequest("No such product!")
    return render_template("products/product.html", product_id=product_id, product_name=product_name)
