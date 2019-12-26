from sqlalchemy import create_engine, \
    Column, Integer, ForeignKey, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(16), nullable=False)
    text = Column(Text, nullable=False)
    is_publised = Column(Boolean, default=False)

    user = relationship(User, back_populates="posts")


if __name__ == '__main__':
    engine = create_engine('sqlite:///blog.db')
    Base.metadata.create_all(engine)

