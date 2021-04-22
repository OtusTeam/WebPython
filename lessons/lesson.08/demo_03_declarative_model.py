from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///example-03.db", echo=True)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False, default="", server_default="")
    is_staff = Column(Boolean, nullable=False, default=False, server_default="0")


if __name__ == '__main__':
    Base.metadata.create_all()
