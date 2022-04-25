from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from werkzeug.exceptions import BadRequest, NotFound
from views.forms.products import ProductForm

products_app = Blueprint("products_app", __name__)


PRODUCTS = {
    1: "Laptop",
    2: "Desktop",
    3: "Tablet",
}


@products_app.get("/", endpoint="list")
def list_products():
    # return jsonify(["p1", "p2"])
    # return jsonify(PRODUCTS)
    # return PRODUCTS
    return render_template("products/list.html", products=PRODUCTS.items())


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product(product_id):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"product #{product_id} not found!")
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
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

    # product_name = request.form.get("product-name")
    # if not product_name:
    #     raise BadRequest("Product name is required, please fill `product-name`")

    product_id = len(PRODUCTS) + 1
    PRODUCTS[product_id] = product_name

    url_product = url_for("products_app.details", product_id=product_id)
    flash(f"Created product {product_name}!")
    return redirect(url_product)
