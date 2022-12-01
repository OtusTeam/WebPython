from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db
from views.products import products_app
from views.users import users_app

app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="477b09f3c51a5e498bae69b239560373d22753238ffe7c5c9bbee87b9ccdf687s",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://demouser:demopass@localhost:5432/blog",
    # SQLALCHEMY_DATABASE_URI="sqlite:///./project.db",
    # SQLALCHEMY_ECHO=True,
    # SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

app.register_blueprint(products_app, url_prefix="/products")
app.register_blueprint(users_app, url_prefix="/users")

csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.cli.command("db-create-all")
def db_create_all():
    # products_data = read_products_from_json('filepath.json')
    # products = [
    #     Product(**products_data)
    #     for product_data in products_data
    # ]
    # db.session.add_all(products)
    # db.session.commit()
    # print(db.metadata.tables)
    db.create_all()


@app.route("/")
def root_view():
    username = request.args.get("username")
    print("username:", username)
    return render_template("index.html", username=username)


@app.route("/about/")
def about_view():
    return render_template("about.html")


@app.route("/items/<item_id>/")
def get_item_string(item_id: str):
    return {
        "item": {"name": item_id.title()},
    }


def print_request():
    print(request)
    print(request.args)
    print(request.headers["accept"])


@app.route("/items/<int:item_id>/")
def get_item(item_id: int):
    return {
        "item": {"id": item_id},
    }


@app.route("/hello/")
def hello_name():
    print_request()
    # name = request.args.get("name") or "World"
    name = request.args.get("name", "World")

    return {
        "message": f"Hello {name}!",
        # "name": request.args.get("name"),
        # "ids": request.args.getlist("ids"),
        # "args": request.args.to_dict(),
        # "args(multi)": request.args.to_dict(flat=False),
    }
