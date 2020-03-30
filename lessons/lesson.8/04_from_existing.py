from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///myblog.db')
metadata = MetaData(bind=engine)

if __name__ == '__main__':
    posts_table = Table(
        'posts',
        metadata,
        autoload=True,
    )
    print([c.name for c in posts_table.columns])
