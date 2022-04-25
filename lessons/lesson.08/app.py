from flask import Flask, request
from views.products import products_app

app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="asdfghjk",
)

app.register_blueprint(products_app, url_prefix="/products")


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
