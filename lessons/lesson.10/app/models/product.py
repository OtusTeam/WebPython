from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Text
from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    # description = Column(Text, nullable=False, default="", server_default="")

    # @classmethod
    # def create_product(cls, session, name: str):
    #     product = Product(name=name)
    #     session.add(product)
    #     session.commit()
    #     return product

    if TYPE_CHECKING:
        query: Query


# class ProductDAL:
#     """
#     Data Access Layer
#     """
#     def __init__(self, session):
#         self.session = session
#
#     def create_product(self, name: str):
#         product = Product(name=name)
#         self.session.add(product)
#         self.session.commit()
#         return product
