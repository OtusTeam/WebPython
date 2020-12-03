from flask import Flask, request, jsonify, render_template

from views.products import product_app


app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("environ", request.environ)
        print("host", request.host)
        print("data", request.data)
        print("form", request.form)
        print("json", request.json)
        return "Hello POST!"
    name = request.args.get("name") or "World"
    return render_template("index.html", name=name)


# app.add_url_rule("/", view_func=index)


@app.route("/prdct/<int:product_id>/")
@app.route("/prdct/<string:product_id>/")
def get_product(product_id):
    return jsonify(product_id=product_id)


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
