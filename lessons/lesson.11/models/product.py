from werkzeug.exceptions import NotFound
from sqlalchemy import Column, Integer, String, Boolean
from models.database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_new = Column(Boolean, nullable=False, default=False)
    deleted = Column(Boolean, nullable=False, default=False, server_default="0")

    @classmethod
    def get_product_by_id(cls, product_id, deleted=False):
        # product = Product.query.filter(Product.id == product_id).one_or_none()
        # .with_for_update()
        product = cls.query.filter_by(deleted=deleted, id=product_id).one_or_none()
        if product is None:
            raise NotFound(f"Product #{product_id} not found!")
        return product
