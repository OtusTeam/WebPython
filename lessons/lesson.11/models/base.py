from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declared_attr, declarative_base

engine = create_engine("sqlite:///myblog.db")


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"myblog_{cls.__name__.lower()}"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base, bind=engine)
