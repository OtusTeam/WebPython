from flask import Blueprint

cart_app = Blueprint('cart_app', __name__)


@cart_app.route('/')
def cart():
    return '<h1>Cart</h1>'


@cart_app.route('/pay/')
def cart_pay():
    return '<h1>PAY</h1>'
