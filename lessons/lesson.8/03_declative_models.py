from sqlalchemy import create_engine, Table, Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///myblog.db')
Base = declarative_base(bind=engine)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(40), nullable=False)
    text = Column(Text, nullable=False)
    is_published = Column(Boolean, nullable=False, default=False)


if __name__ == '__main__':
    Base.metadata.create_all()
