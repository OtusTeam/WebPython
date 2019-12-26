from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///session.db')

# Проверить в нескольких потоках scope
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
# без scope
# Session = session_factory

if __name__ == '__main__':
    session1 = Session()
    session2 = Session()
    print(session1 is session2)
