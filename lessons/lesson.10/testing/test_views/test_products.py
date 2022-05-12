from http import HTTPStatus
from time import time

from flask import url_for

from models import Product


def test_add_product(client):
    product_name = f"product_{time()}"
    create_product_url = url_for("products_app.add")
    response = client.post(create_product_url, json={"product-name": product_name})
    assert response.status_code < HTTPStatus.BAD_REQUEST
    product: Product = Product.query.filter(Product.name == product_name).one()
    assert product.is_new is False
