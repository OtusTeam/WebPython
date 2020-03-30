from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean

engine = create_engine('sqlite:///myblog.db')
metadata = MetaData()

post_table = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('title', String(40), nullable=False),
    Column('text', Text, nullable=False),
    Column('is_published', Boolean, nullable=False, default=False),
)

if __name__ == '__main__':
    metadata.create_all(engine)
