from flask import Flask, request, render_template

from products_views import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")


class Config:
    DEBUG = True


app.config.from_object(Config)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        return render_template("index.html", name=request.args.get("name"))
    return "<h2>Hello post!</h2>"


def main():
    app.run()


if __name__ == '__main__':
    main()
