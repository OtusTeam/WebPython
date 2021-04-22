from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    create_engine,
)
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///example-01.db", echo=True)
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True, nullable=False, default=""),
    Column("is_staff", Boolean, nullable=False, default=False, server_default="0"),
)


class User:
    def __init__(self, id, username, is_staff):
        self.id = id
        self.username = username
        self.is_staff = is_staff


mapper(User, users_table)
