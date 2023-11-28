# |
from flask import Flask, render_template, request
from werkzeug.exceptions import NotFound
from views.contacts import contacts

app = Flask(__name__)
app.register_blueprint(contacts)

PRODUCTS = {
    1: 'Laptop',
    2: 'Smartphone',
    3: 'Notebook',
}

# PRODUCTS = {}


@app.route("/")
def index():
    print('REQUEST')
    print(request)
    print(request.headers)
    print(request.args)
    print(request.headers['user-agent'])
    return render_template('index.html', products=PRODUCTS)


@app.route('/product/<int:product_id>/')
def product_detail(product_id):
    # product = PRODUCTS.get(product_id)
    try:
        product = PRODUCTS[product_id]
    except KeyError:
        raise NotFound
    return render_template('product.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)
