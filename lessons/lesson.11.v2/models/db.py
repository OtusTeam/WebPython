from sqlalchemy.orm import sessionmaker, scoped_session
from .engine import engine

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
