from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import declarative_base


DB_URL = "sqlite:///example-02.db"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


def create_table():
    sql = """
    CREATE TABLE users (
        id INTEGER NOT NULL, 
        username VARCHAR(30), 
        is_staff BOOLEAN NOT NULL, 
        created_at DATETIME, 
        PRIMARY KEY (id), 
        UNIQUE (username)
    )
    """
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_table()

