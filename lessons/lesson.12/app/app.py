from uuid import uuid4
from flask import Flask, request, jsonify, render_template, g
from flask_migrate import Migrate

import config
from models.database import db
from views.products import product_app


app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")

app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
Migrate(app, db, compare_type=True)


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
    return render_template("index.html", name=name, public_key=g.public_key)


@app.before_request
def add_data_to_g():
    g.public_key = uuid4()


@app.route("/prdct/<int:product_id>/")
@app.route("/prdct/<string:product_id>/")
def get_product(product_id):
    return jsonify(product_id=product_id)


@app.cli.command('init-db', with_appcontext=True)
def initialize_db():
    """
    Create initial sqlite db
    # not used due to Flask-Migrate
    """
    print("Do init db")
    db.create_all()
    print("init db done")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
