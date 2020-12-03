from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template, request, redirect, url_for

product_app = Blueprint("product_app", __name__)


PRODUCTS = {
    1: "Phone",
    2: "Laptop",
    3: "Tablet",
    4: "Watch",
}

ids = iter(range(len(PRODUCTS) + 1, 1000))


# def index()
@product_app.route("/", endpoint="products_list")
def products_list():
    return render_template("products/products_list.html", products=PRODUCTS)


@product_app.route("/<int:product_id>/", endpoint="product_detail")
def product_detail(product_id):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise NotFound(f"Product #{product_id} not found!")

    # object = Product.query.filter(id=product_id).one_or_none()
    # if object is None:
    #     raise NotFound

    return render_template(
        "products/product_detail.html",
        product_id=product_id,
        product_name=product_name,
    )


@product_app.route("/add/", methods=["GET", "POST"], endpoint="add_product")
def product_add():
    if request.method == "GET":
        return render_template("products/add_product.html")

    PRODUCTS[next(ids)] = request.form.get("product_name")
    return redirect(url_for("product_app.products_list"))
