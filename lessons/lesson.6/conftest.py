from pytest import fixture
from db_helper import get_connection, get_engine


@fixture(scope="module")
def engine():
    engine = get_engine("sqlite:///test/:memory:")
    return engine


@fixture(scope="module")
def connection(engine):
    conn = get_connection(engine)
    print("new test connection")
    yield conn
    conn.close()
    print("closed test connection")
