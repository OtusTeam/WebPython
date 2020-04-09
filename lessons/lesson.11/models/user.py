import hashlib
from flask_login import UserMixin
from sqlalchemy import Column, String

from .base import Base


class User(Base, UserMixin):
    username = Column(String(30), nullable=False, unique=True)
    _password = Column("password", String(32), nullable=False)
    # posts = relationship('Post', back_populates='user')

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = self.hash_password(value)

    @classmethod
    def hash_password(cls, value: str) -> str:
        """
        Hashes the password
        :param value:
        :return:
        """
        return hashlib.md5(value.encode("utf-8")).hexdigest()

    def __repr__(self):
        return f'<User #{self.id} {self.username}>'
