from sqlalchemy import create_engine, \
    Column, Integer, ForeignKey, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///blog.db')

# Проверить в нескольких потоках scope
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f'<User #{self.id} {self.username}>'


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(16), nullable=False)
    text = Column(Text, nullable=False)
    is_publised = Column(Boolean, default=False)

    user: User = relationship(User, back_populates="posts", lazy="joined")

    def __repr__(self):
        return f'<Post #{self.id} {self.title}>'


def create_some_data():
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
    """RUN"""
    # create_some_data()
    session = Session()
    q = session.query(Post)

    # print(list(q))
    # print(q.all())
    f: Post = q.first()
    print(f)
    print(f.user)
    print(f.user.username)
