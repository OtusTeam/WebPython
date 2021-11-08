import random
from unittest import mock

from pytest import fixture

from db_helper import (
    User,
    Engine,
    Connection,
    get_engine,
    get_connection,
    get_user,
)


@fixture
def user():
    user = User(str(random.randbytes(8)))
    print("created user", user)
    yield user
    print("delete user", user)
    user.delete()


@fixture(scope="module")
def engine_default():
    return get_engine()


@fixture(scope="module")
def connection_default(engine_default):
    return get_connection(engine_default)


class TestUser:

    def test_update_username(self, user):
        old_username = user.username
        new_username = str(random.randbytes(10))

        user.username = new_username

        assert user.username != old_username


def test_connection(connection_default):
    assert isinstance(connection_default, Connection)
    assert isinstance(connection_default.engine, Engine)


def test_multiple_fixtures(engine_default, connection_default):
    assert connection_default.engine is engine_default


@mock.patch("db_helper.get_engine", autospec=True)
@mock.patch("db_helper.get_connection", autospec=True)
def test_get_user(
    mock_get_connection,
    mock_get_engine,
    user,
):
    print("mock_get_connection", mock_get_connection)
    print("mock_get_engine", mock_get_engine)
    username = user.username

    mock_conn = mock_get_connection.return_value
    print("mock_conn", mock_conn)
    print("mock_conn.get_user", mock_conn.get_user)

    mock_conn.get_user.return_value = user

    result = get_user(username)
    assert result is user

    mock_conn.get_user.assert_called_once_with(username)
    mock_get_engine.assert_not_called()
