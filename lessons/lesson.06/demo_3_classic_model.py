from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///three.db', echo=True)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)

# User.id
#
# user = User()
# user.id = 123
# user.id  # 123


if __name__ == '__main__':
    Base.metadata.create_all()
