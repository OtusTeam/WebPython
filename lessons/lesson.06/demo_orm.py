from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    func, Table,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload

engine = create_engine('sqlite:///orm-example.db', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base(bind=engine)


class CreatedAtMixin:
    created_at = Column(DateTime, nullable=False, server_default=func.now())


class User(CreatedAtMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" username={self.username!r}," \
               f" is_staff={self.is_staff}," \
               f" created_at={self.created_at})"

    def __repr__(self):
        return str(self)


posts_tags_association_table = Table(
    "posts_tags_association_table",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class Post(CreatedAtMixin, Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, server_default="")

    author_id = Column(ForeignKey(User.id), nullable=False, unique=False)
    author = relationship("User", back_populates="posts")

    tags = relationship(
        "Tag",
        back_populates="posts",
        secondary=posts_tags_association_table,
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" title={self.title!r}" \
               f" created_at={self.created_at})"

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    posts = relationship(
        "Post",
        back_populates="tags",
        secondary=posts_tags_association_table,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


def create_admin_user():
    session = Session()

    user_admin = User(username="admin", is_staff=True)
    print(user_admin)

    session.add(user_admin)
    session.commit()
    print(user_admin)

    session.close()


def create_users():
    session = Session()

    user_john = User(username="john")
    user_sam = User(username="sam")
    print(user_john)
    print(user_sam)

    session.add(user_john)
    session.add(user_sam)
    session.commit()

    print(user_john)
    print(user_sam)

    session.close()


def get_all_users():
    session = Session()

    users = session.query(User).all()

    print("users:", users)

    session.close()


def get_user_by_pk():
    session = Session()

    user_one = session.get(User, 1)
    print(user_one)

    session.close()


def get_user_by_username():
    session = Session()

    # user_sam = session.query(User).filter_by(username="samuel").one()
    user_sam = session.query(User).filter_by(username="sam").one_or_none()
    # user_sam = session.query(User).filter_by(username="sam").first()
    # user_sam = session.query(User).filter_by(username="sam").all()[0]
    print(user_sam)

    session.close()


def get_users_by_username():
    session = Session()

    users = session.query(User).filter(
        User.username.in_(["sam", "john"])).all()
    print(users)

    session.close()


def create_posts_for_users():
    session = Session()
    user_sam = session.query(User).filter_by(username="sam").one()
    user_john = session.query(User).filter_by(username="john").one()

    post_1 = Post(title="Flask lesson", author=user_sam)
    post_2 = Post(title="Django lesson", author=user_john)

    session.add(post_1)
    session.add(post_2)
    session.commit()

    session.close()


def get_all_posts_with_authors():
    session = Session()

    posts = session.query(Post).options(joinedload(Post.author)).all()

    for post in posts:  # type: Post
        print("post", post)
        print("post author", post.author)

    session.close()


def get_all_users_with_posts():
    session = Session()

    users = session.query(User).options(joinedload(User.posts)).all()

    for user in users:  # type: User
        print("user", user)
        print("user's posts", user.posts)

    session.close()


def get_all_lessons_posts():
    session = Session()

    posts_lessons = (
        session.query(Post)
        .filter(Post.title.ilike("%lesson%"))
        .options(joinedload(Post.author))
        .all()
    )

    for post in posts_lessons:  # type: Post
        print("post", post)
        print("post author", post.author)

    session.close()


def get_all_lessons_authors():
    session = Session()

    users_lessons_authors = (
        session.query(User)
        .join(Post)
        .filter(Post.title.ilike("%lesson%"))
    )

    for user in users_lessons_authors:
        print("user", user)

    session.close()


def create_tags():
    session = Session()

    tags_names = ["news", "python", "flask", "django"]

    tags = [Tag(name=name) for name in tags_names]

    for tag in tags:
        session.add(tag)

    session.commit()

    for tag in tags:
        print(tag.id, tag)

    session.close()


def assign_tags():
    session = Session()

    tags = session.query(Tag).all()
    tags_map = {tag.name: tag for tag in tags}
    tag_python = tags_map.pop("python")

    posts = session.query(Post).options(joinedload(Post.tags)).all()

    for post in posts:  # type: Post
        print("post", post, "with tags", post.tags)
        for tag_name, tag in tags_map.items():
            if tag_name in post.title.lower():
                post.tags.append(tag)
                print("assigned tag", tag, "to post", post)
        post.tags.append(tag_python)

    session.commit()

    posts = session.query(Post).options(joinedload(Post.tags)).all()

    for post in posts:  # type: Post
        print("post", post, "with tags", post.tags)

    session.close()


def show_posts_with_tags_and_authors():
    session = Session()

    posts = (
        session.query(Post)
        .options(
            joinedload(Post.tags)
        )
        .options(
            joinedload(Post.author)
        )
        .all()
    )

    for post in posts:  # type: Post
        print("++post", post)
        print("with tags", post.tags)
        print("and author", post.author)

    session.close()


def find_users_by_tags():
    session = Session()

    users = (
        session.query(User)
        .join(User.posts)
        .join(Post.tags)
        .filter(Tag.name == "news")
        .all()
    )

    for user in users:
        print("user", user)

    session.close()


def main():
    Base.metadata.create_all()
    create_admin_user()
    create_users()
    get_all_users()
    get_user_by_pk()
    get_user_by_username()
    get_users_by_username()
    create_posts_for_users()
    get_all_posts_with_authors()
    get_all_users_with_posts()
    get_all_lessons_posts()
    get_all_lessons_authors()
    create_tags()
    assign_tags()
    show_posts_with_tags_and_authors()
    find_users_by_tags()


if __name__ == '__main__':
    main()
