from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    Text,
    DateTime,
    false,
)

from sqlalchemy.orm import declarative_base

DB_URL = "sqlite:///example2.db"
# `True` ONLY FOR DEBUG!
DB_ECHO = True
# DB_ECHO = False

engine = create_engine(url=DB_URL, echo=DB_ECHO)

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    archived = Column(Boolean, default=False, server_default=false())
    created_at = Column(DateTime, default=datetime.utcnow)

    # extra = Column("extra_data", JSON)
    # _password = Column("password", String)
    #
    # @property
    # def password(self) -> str:
    #     return self.password
    #
    # @password.setter
    # def password(self, value):
    #     self._password = hash(value)


def main():
    Base.metadata.drop_all()
    Base.metadata.create_all()


if __name__ == "__main__":
    main()
