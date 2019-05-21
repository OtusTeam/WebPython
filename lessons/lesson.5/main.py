from flask import Flask, request, render_template

from products_views import products_app
from cart_views import cart_app


app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products/')
app.register_blueprint(cart_app, url_prefix='/cart/')


@app.route('/')
@app.route('/<int:user_id>/')
@app.route('/<float:user_id>/')
@app.route('/<name>/')
def index_page(name=None, user_id=None):
    response = render_template(
        'index.html',
        name=name or 'World',
        user_id=user_id,
    )
    return response


app.run('localhost', 8080, debug=True)
