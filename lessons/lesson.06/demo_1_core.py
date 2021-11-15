from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
)

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///one.db', echo=True)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
)


if __name__ == '__main__':
    metadata.create_all(bind=engine)
