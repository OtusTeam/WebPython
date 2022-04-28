from flask import Flask, render_template, request, current_app
from flask_migrate import Migrate
from models import db
from views.products import products_app

app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="asdfghjk",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://user:password@localhost:5432/shop",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    # SQLALCHEMY_ECHO=True,
    SQLALCHEMY_ECHO=False,
)
app.register_blueprint(products_app, url_prefix="/products")

db.init_app(app)
migrate = Migrate(app, db)


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template("errors/500.html"), 500

# with app.app_context():
#     print(current_app)
#     print(current_app.config)


#

# @app.cli.command("create-schemas", help="Creates all known db schemas")
# def create_all_schemas():
#     print("create all tables...")
#     db.create_all()
#     print("created all tables!")
#
#
# @app.cli.command("drop-schemas", help="Drops all known db schemas")
# def create_all_schemas():
#     print("drop all tables...")
#     db.drop_all()
#     print("dropped all tables!")


@app.cli.command("show-sqla-configs")
def show_sqla_configs():
    # sqla_configs = {
    #     key: value
    #     for key, value in current_app.config.items()
    #     if key.startswith("SQLALCHEMY_")
    #  }
    # print(sqla_configs)

    for key, value in current_app.config.items():
        if key.startswith("SQLALCHEMY_"):
            print(f"{key}={value!r}")
#


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return {"message": "Hello, World!", "method": request.method}


# def helper():
#     print(request)

@app.get("/hello/")
def handle_hello():
    # helper()
    name = request.args.get("name", "OTUS")
    return {"name": name}


@app.get("/hello/<name>/")
def hello_name(name):
    return {"msg": f"Hello {name}!"}


@app.get("/authors/<int:author_id>/")
def get_author_by_id(author_id: int):
    return {
        "author_id": author_id,
    }


@app.get("/authors/<int:author_id>/books/<int:book_id>/")
def get_author_book_by_ids(author_id: int, book_id: int):
    return {
        "author_id": author_id,
        "book_id": book_id,
    }


if __name__ == '__main__':
    app.run(debug=True)
