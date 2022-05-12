import logging

from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from views.forms.product import ProductForm
from models import db, Product


log = logging.getLogger(__name__)

products_app = Blueprint("products_app", __name__)


PRODUCTS = {
    1: "Laptop",
    2: "Desktop",
    3: "Tablet",
}


@products_app.get("/", endpoint="list")
def list_products():
    products: list[Product] = Product.query.all()
    return render_template("products/list.html", products=products)


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product(product_id):
    # product = Product.query.filter_by(id=product_id).one_or_none()
    # if product is None:
    #     raise NotFound(f"product #{product_id} not found!")

    product: Product = Product.query.get_or_404(product_id, description=f"product #{product_id} not found!")
    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        print(form.errors)
        return render_template("products/add.html", form=form), 400

    product_name = form.data["name"]
    product_is_new = bool(form.data.get("is_new"))
    # product_is_not_new = not form.data.get("is_new")
    # product_is_new = not not form.data.get("is_new")

    # product_name = request.form.get("product-name")
    # if not product_name:
    #     raise BadRequest("Product name is required, please fill `product-name`")

    product = Product(name=product_name, is_new=product_is_new)
    db.session.add(product)
    try:
        db.session.commit()
    except IntegrityError:
        log.exception("Could not add product %s", product)
        db.session.rollback()
        raise BadRequest(f"could not save product, probably the name `{product_name}` is not unique")
    except DatabaseError:
        log.exception("Could not save product %s", product)
        db.session.rollback()
        flash("errooro!", category="error")
        raise InternalServerError("Could not save product due to unexpected error!")

    url_product = url_for("products_app.details", product_id=product.id)
    flash(f"Created product {product_name}!")
    return redirect(url_product)
