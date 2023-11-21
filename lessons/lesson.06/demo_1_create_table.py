from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
)

from config import engine

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String, nullable=True, unique=True),
)


def main():
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
