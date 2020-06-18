from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean

engine = create_engine("sqlite:///example.db")
metadata = MetaData()


posts_table = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("title", String(50), nullable=False),
    Column("text", Text, nullable=False),
    Column("is_published", Boolean, nullable=False, default=False, server_default="0"),
)


if __name__ == '__main__':
    metadata.create_all(engine)
