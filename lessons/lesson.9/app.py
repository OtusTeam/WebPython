from flask import Flask, request, render_template

from products_views import products_app
from cart_views import cart_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products')
app.register_blueprint(cart_app, url_prefix='/cart')

app.config.update(
    DEBUG=True,
)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'GET':
        # return 'Hello world!'
        return render_template('index.html')
    return f'Hello request {request.method}'


@app.route('/', methods=['PATCH'])
def index_patch():
    return 'Hello PATCH!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
