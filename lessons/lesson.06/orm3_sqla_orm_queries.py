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
    func,
)

from sqlalchemy.orm import (
    declarative_base,
    Session as SessionType,
    sessionmaker,
    scoped_session,
)

# DB_URL = "postgresql+pg8000://user:password@host:port/dbname"
DB_URL = "postgresql+psycopg2://demouser:demopass@localhost:5432/blog"

# `True` ONLY FOR DEBUG!
DB_ECHO = True
# DB_ECHO = False

engine = create_engine(url=DB_URL, echo=DB_ECHO)

Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    # def __init__(self, username: str):
    #     # super().__init__()
    #     self.username = username

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    archived = Column(Boolean, default=False, server_default=false())
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, " \
               f"archived={self.archived}, created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)
    print("user", user)
    session.add(user)
    print("user (added)", user)
    session.commit()
    print("saved user", user)
    return user


def create_users(session: SessionType, *usernames: str) -> list[User]:
    users = []
    for username in usernames:
        user = User(username=username)
        session.add(user)
        users.append(user)

    session.commit()

    return users


def get_all_users(session: SessionType) -> list[User]:
    users = session.query(User).order_by(User.id).all()
    print("users:", users)
    return users


def get_user_by_username(session: SessionType, username: str) -> User | None:
    # user = session.query(User).filter_by(username=username).first()
    # user = session.query(User).filter_by(username=username).one()
    user = session.query(User).filter_by(username=username).one_or_none()
    print("user:", user)
    return user


def get_user_by_id(session: SessionType, user_id: int) -> User | None:
    user = session.get(User, user_id)
    print("user:", user)
    return user


def get_users_by_username_match(session: SessionType, username_part: str) -> list[User]:
    users = session.query(User).filter(User.username.ilike(f"%{username_part}%")).all()
    print("user:", users)
    return users


def main():
    # Base.metadata.drop_all()
    # Base.metadata.create_all()

    session: SessionType = Session()

    # create_user(session, "john")
    # create_user(session, "sam")

    # create_users(session, "bob", "alice", "kate", "nick")
    # get_all_users(session)
    # get_user_by_username(session, "bob")
    get_user_by_username(session, "jack")
    # get_user_by_id(session, 1)
    # get_user_by_id(session, 100)

    # get_users_by_username_match(session, "a")
    # get_users_by_username_match(session, "j")
    # get_users_by_username_match(session, "x")

    session.close()


if __name__ == '__main__':
    main()
