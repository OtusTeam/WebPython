import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models import db, Product

products_app = Blueprint("products_app", __name__)


@products_app.route("/", endpoint="list")
def list_products():
    # db.session.query(Product).all()
    products = Product.query.order_by(Product.id).all()

    return render_template(
        "products/list.html",
        products=products,
    )


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        raise NotFound(f"no product with id #{product_id}")
    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("field product-name is required!")

    product = Product(name=product_name)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError as e:
        logging.debug("integrity error %s", e)
        raise BadRequest("Could save new product probably because name is not unique")
    except DatabaseError:
        logging.exception("Could not save product with name %r", product_name)
        raise InternalServerError("Could not save product")

    return redirect(url_for("products_app.details", product_id=product.id))
