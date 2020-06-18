from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("sqlite:///example.db")
metadata = MetaData(bind=engine)

if __name__ == '__main__':
    posts_table = Table(
        "posts",
        metadata,
        autoload=True,
    )
    for c in posts_table.columns:
        print(f"Column {c.name!r}:", repr(c))
