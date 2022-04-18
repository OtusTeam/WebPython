from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import (
    declarative_base,
    scoped_session,
    sessionmaker,
    Session as SessionType,
)


DB_URL = "postgresql+pg8000://username:passwd!@localhost:5432/blog"
# DB_URL = "postgresql+psycopg2://username:passwd!@localhost:5432/blog"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)


session_factory = sessionmaker(bind=engine)

# Session = session_factory()
Session = scoped_session(session_factory)

# session = Session()


class Base:
    id = Column(Integer, primary_key=True)

    # @declared_attr
    # def query(cls):
    #     return Session().query(cls)


Base = declarative_base(bind=engine, cls=Base)


class User(Base):
    __tablename__ = "users"

    username = Column(String(30), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def promote(self):
        self.is_staff = True


    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"is_staff={self.is_staff}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)


def query_all_users(session: SessionType) -> list[User]:
    users = session.query(User).all()
    print(users)
    return users


def create_user(session: SessionType, username: str) -> User:

    user = User(username=username)
    print("create user", user)

    # with session.begin():

    session.add(user)
    session.commit()

    print("saved", user)

    return user


def query_user(session: SessionType, username: str) -> User:

    user = session.query(User).filter_by(username=username).one()
    # user = session.query(User).filter_by(username=username).one_or_none()
    user = session.query(User).filter_by(username=username).first()
    print("found user", user)
    return user


def get_user_by_id(session: SessionType, user_id: int) -> User:
    # user = session.query(User).filter_by(id=user_id).one_or_none()
    user = session.get(User, user_id)
    print("got user", user)
    return user


def find_users_match_username(session: SessionType, name_part: str) -> list[User]:
    q_users = session.query(User)
    q_users_matching_username = q_users.filter(
        User.username.like(f"%{name_part}%"),
    )
    users = q_users_matching_username.all()
    print(f"found users for {name_part!r}:", users)
    return users


def promote_user(session: SessionType, user: User) -> User:

    print("before", user)
    user.promote()
    print("after", user)

    session.commit()
    print("after commit", user)

    return user



def main():
    sql = """
    CREATE TABLE users (
        id SERIAL NOT NULL, 
        username VARCHAR(30), 
        is_staff BOOLEAN NOT NULL, 
        created_at TIMESTAMP WITHOUT TIME ZONE, 
        PRIMARY KEY (id), 
        UNIQUE (username)
    )
    """
    # Base.metadata.create_all()

    session: SessionType = Session()

    # create_user(session, "sam")
    # create_user(session, "samuel")
    # query_all_users(session)
    # query_user(session, "sam")
    # query_user(session, "john")
    # get_user_by_id(session, 1)
    # user = get_user_by_id(session, 2)
    # user = get_user_by_id(session, 3)
    # find_users_match_username(session, "sam")
    # find_users_match_username(session, "john")

    # promote_user(session, user)

    print("users count:", session.query(User).count())
    print("users count:", session.query(User.id).count())

    session.close()


if __name__ == '__main__':
    main()
