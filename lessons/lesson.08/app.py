from flask import Flask, url_for

from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")


@app.route("/")
def index_view():
    return "Hello world!!!"


@app.route("/info/")
def info_view():
    return {
        "routes": {
            "url_for('hello_user')": url_for("hello_user"),
            "url_for('hello_user', username='OTUS')": url_for(
                "hello_user", username="OTUS"),
        }
    }


@app.route("/hello/")
@app.route("/hello/<username>/")
def hello_user(username="Wold"):
    return f"Hello {username}!"


@app.route("/items/<int:item_id>/")
def get_item_by_id(item_id):
    return {"item": item_id}


# if __name__ == '__main__':
#     app.run()
