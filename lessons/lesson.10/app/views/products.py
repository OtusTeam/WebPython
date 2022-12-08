from http import HTTPStatus

from flask import Blueprint, render_template, request, url_for, redirect, flash

from models import db, Product
from views.forms.product import ProductForm

# products_app = Blueprint("products_app", __name__, url_prefix="/products")
products_app = Blueprint("products_app", __name__)


@products_app.get("/", endpoint="list")
def products_list():
    products = Product.query.all()
    return render_template("products/list.html", products=products)


@products_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/create.html", form=form)

    if not form.validate_on_submit():
        return render_template(
            "products/create.html",
            form=form,
        ), HTTPStatus.BAD_REQUEST

    name = form.name.data
    product = Product(name=name)
    db.session.add(product)
    db.session.commit()

    flash(f"Product #{product.id} created!")
    url = url_for("products_app.details", product_id=product.id)
    # url = url_for("products_app.list")
    return redirect(url)


@products_app.get("/<int:product_id>/", endpoint="details")
def product_details(product_id: int):
    # product = Product.query.get(product_id)
    product = Product.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )
    # product = Product.query.filter(Product.id == product_id).one_or_none()
    # product = Product.query.filter(Product.id == product_id).one_or_404()

    return render_template(
        "products/details.html",
        product=product,
    )


# @products_app.get("/")
# def products_list():
#     return PRODUCTS
