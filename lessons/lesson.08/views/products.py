from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

# products_app = Blueprint("products_app", __name__, url_prefix="/products")
products_app = Blueprint("products_app", __name__)


PRODUCTS = {
    1: "Laptop",
    2: "Desktop",
    3: "Smartphone",
}


@products_app.get("/", endpoint="list")
def products_list():
    return render_template("products/list.html", products=PRODUCTS)


@products_app.get("/<int:product_id>/", endpoint="details")
def product_details(product_id: int):
    product_name = PRODUCTS.get(product_id)
    # if not product_name
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


# @products_app.get("/")
# def products_list():
#     return PRODUCTS
