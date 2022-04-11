import random
from string import ascii_lowercase
from unittest import mock

from pytest import fixture, param, mark

from db_helper import (
    User,
    Engine,
    Connection,
    get_user,
    get_engine,
    get_connection,
)


@fixture
def username() -> str:
    letters = random.choices(ascii_lowercase, k=8)
    username = "".join(letters)
    return username


@fixture
def user(username) -> User:
    user = User(username)
    print("created user", user)
    # return user
    yield user
    user.delete()


@fixture
def engine_default() -> Engine:
    return get_engine()


@fixture
def connection_default(engine_default) -> Connection:
    return get_connection(engine=engine_default)


class TestUser:
    def test_init(self):
        username = "spam-and-eggs"
        user = User(username)
        assert user.username == username

    def test_set_age(self, user):
        age = random.randint(13, 100)
        assert user.age != age
        user.set_age(age)
        assert user.age == age

    def test_delete(self, user):
        assert user.delete()


def test_connection_default(connection_default, engine_default):
    assert isinstance(connection_default, Connection)
    assert isinstance(engine_default, Engine)
    assert connection_default.engine is engine_default


# @mark.parametrize("")
@fixture(params=[param(("abc", "qwe")), param(("123", "456"))])
def myfix(request):
    with mock.patch("....") as mocked_smth:
        yield mocked_smth
    # print(request.param)
    # return request.param


# @mark.usefixtures("myfix")
@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(mocked_get_connection, username, user):
    mock_conn = mocked_get_connection.return_value
    mock_conn.get_user.return_value = user
    u = get_user(username)
    assert u is user
    # print(myfix)
