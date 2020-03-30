from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///myblog.db')
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)

    posts = relationship('Post', back_populates='user')

    def allowed_to_post(self):
        """
        :return:
        """
        return True


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(40), nullable=False)
    text = Column(Text, nullable=False)
    is_published = Column(Boolean, nullable=False, default=False)

    user = relationship(User, back_populates='posts')

    def __init__(self, user: User, title: str, text: str):
        """
        :param user:
        :param title:
        :param text:
        """
        if not user.allowed_to_post():
            raise ValueError

        self.user_id = user.id
        self.title = title
        self.text = text


if __name__ == '__main__':
    Base.metadata.create_all()
