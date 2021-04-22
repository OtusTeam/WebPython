from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    create_engine,
    func,
    or_,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session, joinedload

engine = create_engine("sqlite:///example-04.db", echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False, default="", server_default="")
    is_staff = Column(Boolean, nullable=False, default=False, server_default="0")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    posts = relationship("Post", back_populates="user")
    profile = relationship("UserProfile", uselist=False, back_populates="user")

    def __str__(self):
        return f"User #{self.id} ({self.username})"

    def __repr__(self):
        return str(self)


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False, default="", server_default="")
    last_name = Column(String(120), nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)

    user = relationship(User, back_populates="profile")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(90), nullable=False, default="", server_default="")

    # user_id = Column(Integer, ForeignKey(User.id))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship(User, back_populates="posts")

    def __str__(self):
        return f"{self.title} by #{self.user_id}"

    def __repr__(self):
        return str(self)


def create_users():
    session = Session()

    user = User(username="admin", is_staff=True)
    john = User(username="john")

    session.add(user)
    session.add(john)

    session.commit()

    session.close()


def add_profiles():
    session = Session()

    john = session.query(User).filter_by(username="john").one()

    profile = UserProfile(user=john, first_name="John", last_name="Smith")
    # profile = UserProfile(user_id=user.id)

    session.add(profile)
    session.commit()

    session.close()


def show_users_with_related():
    session = Session()

    print("start")
    admin: User = session.query(User).filter_by(username="admin").one()
    print("admin with profile and posts", admin, admin.profile, admin.posts)
    john: User = session.query(
        User,
    ).filter_by(
        username="john",
    ).options(
        joinedload(User.profile),
        joinedload(User.posts),
    ).one()
    print("john with profile and posts", john, john.profile, john.posts)

    session.close()


def create_posts():
    session = Session()

    admin: User = session.query(User).filter_by(username="admin").one()
    john: User = session.query(User).filter_by(username="john").one()

    post_django = Post(title="Django lesson", user=admin)
    post_flask = Post(title="Flask lesson", user=john)
    post_fastapi = Post(title="FastAPI lesson", user=john)

    session.add(post_django)
    session.add(post_flask)
    session.add(post_fastapi)
    session.commit()

    print("admin with posts", admin, admin.posts)
    print("john with posts", john, john.posts)

    session.close()


def demo_filtering():
    johns = Session.query(User).join(UserProfile).filter(
        UserProfile.first_name.ilike("john"),
    ).all()

    print("johns:", johns)

    Session.close()


def demo_filtering2():
    users_flask_or_django = Session.query(
        User,
        Post,
    # ).join(
    #     UserProfile,
    ).join(
        Post,
    ).filter(
        or_(
            Post.title.ilike("%flask%"),
            Post.title.ilike("%django%"),
        ),
    ).options(
        joinedload(User.profile),
        # joinedload(Post),
    ).all()

    print("users with flask or django posts:")

    for user, post in users_flask_or_django:
        print("user", user, user.profile)
        print("his matched post:", post)

    Session.close()


def check_create_name_drop_table():
    user_dt = User(username="john; DROP TABLE users;")
    Session.add(user_dt)
    Session.commit()
    Session.close()


def main():
    # Base.metadata.create_all()
    # create_users()
    # add_profiles()
    # show_users_with_related()
    # create_posts()
    # demo_filtering()
    demo_filtering2()
    # check_create_name_drop_table()


if __name__ == '__main__':
    main()
