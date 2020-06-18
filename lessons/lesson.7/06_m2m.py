from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

engine = create_engine("sqlite:///example_m2m.db")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


posts_tags_table = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"User(id={self.id}, username={self.username})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    is_published = Column(Boolean, nullable=False, default=False, server_default="0")

    user = relationship(User, back_populates="posts")
    tags = relationship("Tag", secondary=posts_tags_table, back_populates="posts")

    def __repr__(self):
        return f"<Post #{self.id} {self.title}"


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False, unique=True)

    posts = relationship("Post", secondary=posts_tags_table, back_populates="tags")

    def __repr__(self):
        return f"<Tag #{self.id} {self.name}>"


def create_users_and_posts_with_tags():
    session = Session()

    # users = session.query(User).filter(User.username == "otus").all()
    # user = session.query(User).filter_by(username="otus").one_or_none()
    # print("user:", user)
    # print("user's posts:", user.posts)
    # post1: Post = user.posts[0]
    # print("post1:", post1.title)
    # print("post user:", post1.user)

    user = User(username="otus")
    session.add(user)
    session.flush()
    print(user)

    post1 = Post(user_id=user.id, title="Flask lesson", text="qwerty")
    post2 = Post(user_id=user.id, title="Django lesson", text="django!", is_published=True)

    session.add(post1)
    session.add(post2)

    tag_news = Tag(name="news")
    tag_python = Tag(name="python")
    tag_flask = Tag(name="flask")
    tag_django = Tag(name="django")
    session.add(tag_news)
    session.add(tag_python)
    session.add(tag_flask)
    session.add(tag_django)

    session.flush()

    post1.tags.extend((tag_news, tag_python, tag_flask))
    post2.tags.extend((tag_python, tag_django))

    #
    session.commit()
    print("Saved use and posts with tags!")

    print("post1.tags:", post1.tags)
    print("post2.tags:", post2.tags)

    print("tag_python.posts", tag_python.posts)
    print("tag_flask.posts", tag_flask.posts)

    session.close()


def show_with_join():
    session = Session()

    q = session.query(
        User,
    ).join(
        Post,
        User.id == Post.user_id,
    ).filter(
        Post.tags.any(Tag.name.ilike("new%"))
    )
    print(q)
    print(q.all())

    session.close()


def main():
    Base.metadata.create_all()
    # create_users_and_posts_with_tags()
    show_with_join()


if __name__ == '__main__':
    main()
