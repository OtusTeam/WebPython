from sqlalchemy import create_engine, \
    MetaData, Table, Column, Integer, String, Text, Boolean
from sqlalchemy.orm import mapper

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


class Post:
    def __init__(self, user_id, title, text, is_published):
        self.user_id = user_id
        self.title = title
        self.text = text
        self.is_published = is_published


mapper(Post, post_table)

if __name__ == '__main__':
    metadata.create_all(engine)
