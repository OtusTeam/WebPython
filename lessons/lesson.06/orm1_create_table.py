from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)

# from sqlalchemy.dialects.postgresql import BOOLEAN, INTEGER, VARCHAR, ARRAY, JSONB


DB_URL = "sqlite:///example-01.db"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(20), unique=True),
    Column("is_staff", Boolean, default=False, nullable=False),
)


# class User:
#     def __init__(self, id: int, username: str, is_staff: bool):
#         self.id = id
#         self.username = username
#         self.is_staff = is_staff


def create_table():
    sql = """
    CREATE TABLE users (
        id INTEGER NOT NULL,
        username VARCHAR(20),
        is_staff BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
    )
    """
    metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_table()
