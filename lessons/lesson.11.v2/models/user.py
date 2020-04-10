import hashlib
from flask_login import UserMixin
from sqlalchemy import Column, String
from . import Base


class User(Base, UserMixin):
    username = Column(String(64), unique=True, nullable=False)
    _password = Column("password", String(32), nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self.hash_password(value)

    @classmethod
    def hash_password(cls, value: str) -> str:
        return hashlib.md5(value.encode("utf-8")).hexdigest()
