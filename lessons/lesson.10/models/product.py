from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    is_new = Column(Boolean, default=False, nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)
