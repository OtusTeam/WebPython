from flask import Blueprint

cart_app = Blueprint('cart_app', __name__)


@cart_app.route('/')
def cart():
    return '<h1>Cart</h1>'


@cart_app.route('/pay/')
def pay():
    return '<h2>PAY</h2>'
