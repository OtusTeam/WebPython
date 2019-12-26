from sqlalchemy import create_engine,\
    Column, Integer, String, Text, Boolean

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(16), nullable=False)
    text = Column(Text, nullable=False)
    is_publised = Column(Boolean, default=False)


if __name__ == '__main__':
    engine = create_engine('sqlite:///blog.db')
    Base.metadata.create_all(engine)

# Table First
# UML First
# Code First
