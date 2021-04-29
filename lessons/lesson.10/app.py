from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

from views.products import products_app

app = Flask(__name__)

app.register_blueprint(products_app)


@app.route("/")
@app.route("/<name>/")
def hello_world(name="World"):
    return render_template("index.html", name=name)


@app.route("/product/<int:product_id>/")
def get_product(product_id):
    return f"product {product_id!r}"


@app.route("/sum/")
def sum_values():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
    except ValueError:
        raise BadRequest("`a` and `b` have to be integers")
    return {"a": a, "b": b, "sum": a + b}


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
