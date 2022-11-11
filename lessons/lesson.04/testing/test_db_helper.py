from random import choices, randint
from string import ascii_letters

from pytest import fixture

from db_helper import (
    User,
    Engine,
    Connection,
    get_engine,
    get_connection,
)


@fixture
def db_url_default() -> str:
    url = "sqlite:///..." + "".join(choices(ascii_letters, k=8))
    # print("created url...", url)
    return url


@fixture
def engine_default(db_url_default: str) -> Engine:
    # print("engine gets url", db_url_default)
    return get_engine(url=db_url_default)


@fixture
def connection_default(engine_default: Engine) -> Connection:
    return get_connection(engine=engine_default)


@fixture
def username() -> str:
    return "".join(choices(ascii_letters, k=8))


@fixture
def user(username: str):
    # user in database
    user = User(username)
    # session.add(user)
    # session.commit()
    yield user
    # remove user from database
    user.delete()
    # session.delete(user)

# """
# a = "abc"
# b = 456
# c = ...
# d = object()
# e = []
# f = {}
# _ = "t"
# """


def test_default_fixtures(db_url_default, engine_default, connection_default):
    print(engine_default, engine_default.url)
    assert isinstance(engine_default, Engine)
    assert engine_default.url == db_url_default
    assert isinstance(connection_default, Connection)
    assert connection_default.engine is engine_default


class TestUser:
    def test_set_age(self, user):
        age = randint(0, 120)
        assert user.age != age
        user.set_age(age)
        assert user.age == age
