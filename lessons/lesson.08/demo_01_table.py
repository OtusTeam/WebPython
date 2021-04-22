from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    create_engine,
)

engine = create_engine("sqlite:///example-01.db", echo=True)
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True, nullable=False, default=""),
    Column("is_staff", Boolean, nullable=False, default=False, server_default="0"),
)


if __name__ == '__main__':
    metadata.create_all(bind=engine)
