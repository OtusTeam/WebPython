from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    func,
)

from .database import db

# from models.database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, server_default="")
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    is_new = Column(Boolean, nullable=False, server_default="FALSE")

    # comment = Column(String(256), nullable=False, server_default="")
