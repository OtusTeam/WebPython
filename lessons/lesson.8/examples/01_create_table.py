from sqlalchemy import MetaData, create_engine, \
    Table, Column, Integer, String, Text, Boolean
engine = create_engine('sqlite:///blog.db')
metadata = MetaData()

post_table = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('title', String(16), nullable=False),
    Column('text', Text, nullable=False),
    Column('is_publised', Boolean, default=False),
)

if __name__ == '__main__':
    metadata.create_all(engine)
