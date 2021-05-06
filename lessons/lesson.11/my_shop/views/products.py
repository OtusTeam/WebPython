from flask import Blueprint, request, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError

from my_shop.models.database import db
from my_shop.models import Product

products_app = Blueprint("products_app", __name__, url_prefix="/products")


@products_app.route("/", endpoint="list")
def products_list():
    products = Product.query.all()
    return render_template(
        "products/products_list.html",
        products=products,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    if request.method == "GET":
        return render_template("products/add_product.html")
    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Product name is required")

    if Product.query.filter_by(name=product_name).count():
        raise BadRequest(
            f"Error adding product {product_name!r}. Product already exists!")

    product_is_new = request.form.get("is-new")
    product = Product(name=product_name, is_new=bool(product_is_new))
    db.session.add(product)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(
            f"Error adding product {product_name!r}.")

    product_url = url_for("products_app.details", product_id=product.id)
    return redirect(product_url)


@products_app.route("/<int:product_id>/", endpoint="details")
def product_details(product_id):
    # product = Product.query.filter(Product.id == product_id).one_or_none()
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product is None:
        raise NotFound(f"Product #{product_id} not found!")

    return render_template(
        "products/product_details.html",
        product=product,
    )
