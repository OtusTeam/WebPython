from flask import Blueprint, render_template, request, redirect, url_for

from models import Product
from models.database import db

product_app = Blueprint("product_app", __name__)

# MVC
# Model
# View
# Controller

# Django - fat models, view, stupid templates


# def index()
@product_app.route("/", endpoint="products_list")
def products_list():
    products = Product.query.filter_by(deleted=False).all()
    return render_template("products/products_list.html", products=products)


@product_app.route("/<int:product_id>/", endpoint="product_detail")
def product_detail(product_id):
    product = Product.get_product_by_id(product_id)

    return render_template(
        "products/product_detail.html",
        product=product,
    )


@product_app.route("/<int:product_id>/delete/", methods=["POST"], endpoint="product_delete")
def product_delete(product_id):
    product = Product.get_product_by_id(product_id)

    product.deleted = True
    db.session.commit()
    return redirect(url_for("product_app.products_list"))


@product_app.route("/add/", methods=["GET", "POST"], endpoint="add_product")
def product_add():
    if request.method == "GET":
        return render_template("products/add_product.html")

    product_name = request.form.get("product_name")
    is_new = bool(request.form.get("is-new"))
    product = Product(name=product_name, is_new=is_new)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for("product_app.products_list"))
