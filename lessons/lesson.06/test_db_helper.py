from unittest import mock

import pytest

from db_helper import (
    User,
    get_engine,
    get_connection,
    get_user,
    Connection,
    Engine,
)


@pytest.fixture
def user():
    user = User("any_username")
    print("inited user", user)
    yield user
    print("delete user", user)
    user.delete()


class TestUser:
    def test_init(self):
        username = "test_username_1"
        user = User(username)
        assert user.username == username

    def test_save(self, user):
        res = user.save()
        assert res is user

    def test_delete(self, user):
        res = user.delete()
        assert res is True


def test_get_connection():
    conn = get_connection()
    assert isinstance(conn, Connection)
    assert isinstance(conn.engine, Engine)


class TestGetUser:

    def test_get_user(self):
        username = "qwerty"
        user = get_user(username)
        assert user.username == username

    @mock.patch("db_helper.get_connection")
    def test_get_user_check_conn(
        self,
        mocked_get_connection,
        user,
    ):
        mocked_conn = mocked_get_connection.return_value
        # mocked_conn_get_user = mocked_conn.get_user
        mocked_conn.get_user.return_value = user
        res_user = get_user(user.username)
        assert res_user is user

        # mocked_get_connection.assert_called_once()
        mocked_get_connection.assert_called_once_with()
        mocked_conn.get_user.assert_called_once_with(username=user.username)


class TestGetEngine:

    # @mock.patch.object(Engine, "check", autospec=True)
    @mock.patch("db_helper.Engine", autospec=True)
    def test_get_engine(self, mocked_Engine):
        url = "sqlite:///db.sqlite3"
        engine = get_engine(url)
        engine.check.assert_called_once_with()
        mocked_Engine.assert_called_once_with(url)
