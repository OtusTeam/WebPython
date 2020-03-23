from unittest import mock

import pytest

from db_helper import create_engine, get_connection, URL, get_admin, Connection


def test_create_engine():
    url = object()
    res = create_engine(url)
    assert res.url is url


@pytest.fixture
def custom_connection():
    conn = Connection(object())
    yield conn
    conn.close()


class TestGetConnection:
    def test_creates_connection(self):
        res = get_connection()
        assert res.engine.url == URL


class TestGetAdmin:
    def test_pure(self):
        res = get_admin()
        assert res.username == 'admin'

    @mock.patch('db_helper.get_connection', autospec=True)
    def test_admin_is_called_from_connection(self, mocked_get_connection):
        res = get_admin()
        assert res is mocked_get_connection.return_value.request_admin.return_value

    @mock.patch.object(Connection, 'request_admin')
    def test_connection_calls_for_admin(self, mocked_request_admin):
        res = get_admin()
        assert res is mocked_request_admin.return_value
        mocked_request_admin.assert_called_once()

    @mock.patch('db_helper.get_connection', autospec=True)
    def test_custom_connection(self, mocked_get_connection, custom_connection):
        mocked_get_connection.return_value = custom_connection
        res = get_admin()
        assert res.username == 'admin'
        mocked_get_connection.assert_called_once_with()
