from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base


engine = create_engine("sqlite:///myapp.db")


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"myapp_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base, bind=engine)
