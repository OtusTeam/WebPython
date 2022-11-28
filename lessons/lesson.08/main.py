from flask import Flask, request, render_template

from views.products import products_app
from views.users import users_app

app = Flask(__name__)

app.config.update(
    ENV="development",
)

app.register_blueprint(products_app, url_prefix="/products")
app.register_blueprint(users_app, url_prefix="/users")


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


if __name__ == "__main__":
    app.run(
        debug=True,
        # use_reloader=True,
        # use_debugger=False,
    )
