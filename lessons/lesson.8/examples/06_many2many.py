from sqlalchemy import create_engine, \
    Table, Column, ForeignKey, Boolean, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///blog.db')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


tags_posts_table = Table(
    'tags_posts',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True),
)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(16), nullable=False)
    text = Column(Text, nullable=False)
    is_publised = Column(Boolean, nullable=False, default=False)
    user = relationship("User", back_populates="posts", lazy="joined")
    tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")

    def __repr__(self):
        return f'<Post #{self.id} {self.title}>'


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")

    def __repr__(self):
        return f'<Tag #{self.id} {self.name}>'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f'<User #{self.id} {self.username}>'


def create_user_and_posts():
    Base.metadata.create_all(engine)
    session = Session()

    user = User(username='suren')
    session.add(user)
    session.flush()

    post1 = Post(user_id=user.id, title='Flask lesson', text='ok, here we go again')
    post2 = Post(user_id=user.id, title='Django lesson', text='again?')
    session.add(post1)
    session.add(post2)

    session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # create_user_and_posts()
    session = Session()
    # print(session.query(Tag).all())
    # print(session.query(Tag).filter_by(id=4).first())

    # tags = session.query(Tag)[:2]
    # post: Post = session.query(Post).first()
    # post.tags.extend(tags)
    # session.commit()

    # post: Post = session.query(Post).first()
    # print(post.tags)
    # tag: Tag = post.tags[0]
    # print(tag.posts)

    # q = session.query(Post).join(User, Post.user_id == User.id)
    # q = session.query(Post).join(User).filter(User.id == 1)
    # print(q.all())

    # q = session.query(Post).join(tags_posts_table)
    q = session.query(Post).join(tags_posts_table).filter(tags_posts_table.c.tag_id == 1)
    # q = session.query(Post).join(tags_posts_table).filter(tags_posts_table.c.tag_id == 2)
    print(q.count(), 'results:', q.all())
    session.execute('INSERT INTO tags (name) VALUES (?)', ('news', ))
