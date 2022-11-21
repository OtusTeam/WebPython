from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    Text,
)

DB_URL = "sqlite:///example1.db"
# `True` ONLY FOR DEBUG!
# DB_ECHO = True
DB_ECHO = False

engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()
# metadata = MetaData(bind=engine)

# # class Table:
# def init(self, table_name, metadata, *columns):
#     # self.init_cols(columns)
#     # self.post_init()
#     metadata.register(self)


authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True, nullable=False),
    Column("email", String(200), unique=True),
    Column("bio", Text),
)


def main():
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
