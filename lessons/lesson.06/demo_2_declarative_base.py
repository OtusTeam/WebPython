from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
)
from sqlalchemy.orm import DeclarativeBase

from config import engine


# from sqlalchemy.orm import declarative_base

# Base = declarative_base()


class Base(DeclarativeBase):
    pass


# new style -> pydantic
# old style
class Author(Base):
    __tablename__ = "cool_authors"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    address = Column(String, nullable=True, unique=False)


def main():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
