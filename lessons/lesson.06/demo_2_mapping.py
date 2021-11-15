from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)

from sqlalchemy.orm import mapper

engine = create_engine('sqlite:///two.db', echo=True)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("is_staff", Boolean, nullable=False, default=False),
)


class User:
    def __init__(self, id: int, username: str, is_staff: bool):
        self.id = id
        self.username = username
        self.is_staff = is_staff


# user_admin = User(1, "admin", True)
# user_john = User(123, "john", False)
#
# user_admin.id
# user_john.id

mapper(User, users_table)

if __name__ == '__main__':
    metadata.create_all(bind=engine)
