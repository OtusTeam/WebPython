import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

tags_posts_table = sqlalchemy.Table('tags_posts', Base.metadata,
    sqlalchemy.Column('post_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('posts.id')),
    sqlalchemy.Column('tag_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('tags.id')),
)

class Post(Base):
    __tablename__ = 'posts'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    title = sqlalchemy.Column(sqlalchemy.String(16))
    text = sqlalchemy.Column(sqlalchemy.Text)
    is_publised = sqlalchemy.Column(sqlalchemy.Boolean)
    user = relationship("User", back_populates="posts", lazy='joined')
    tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")


class Tag(Base):
    __tablename__ = 'tags'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    posts = relationship("Post", back_populates="user")



# echo - режим дебага
engine = sqlalchemy.create_engine('sqlite:///blog.db', echo=False)
Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()

# создание 1-го поста
# post_info = {'id': 1, 'title': 'foo post'}
# session.add(Post(**post_info))
# session.commit()