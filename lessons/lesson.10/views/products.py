from flask import Blueprint, request, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest

products_app = Blueprint("products_app", __name__, url_prefix="/products")


PRODUCTS = {
    1: "Smartphone",
    2: "Tablet",
    3: "Laptop",
}

idx = iter(range(len(PRODUCTS) + 1, 100))


@products_app.route("/", endpoint="list")
def products_list():
    return render_template(
        "products/products_list.html",
        products=PRODUCTS,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    if request.method == "GET":
        return render_template("products/add_product.html")
    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Product name is required")

    index = next(idx)
    PRODUCTS[index] = product_name
    product_url = url_for("products_app.details", product_id=index)
    return redirect(product_url)


@products_app.route("/<int:product_id>/", endpoint="details")
def product_details(product_id):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")

    return render_template(
        "products/product_details.html",
        product_id=product_id,
        product_name=product_name,
    )
