from unittest import mock
from db_helper import get_user, User


class TestGetUser:
    def test_get_user_raw(self):
        username = "qwerty"
        user = get_user(username)
        assert isinstance(user, User)
        assert user.username == username

    @mock.patch("db_helper.get_connection", autospec=True)
    def test_get_user_from_test_db(self, mocked_get_connection, connection):
        mocked_get_connection.return_value = connection
        username = "qwerty"
        user = get_user(username)
        assert isinstance(user, User)
        assert user.username == username

    @mock.patch("db_helper.get_connection", autospec=True)
    def test_get_user_no_db_request(self, mocked_get_connection):
        username = "qwerty"
        res = get_user(username)
        mocked_get_connection.assert_called_once_with()
        mocked_get_connection.return_value.get_user.assert_called_once_with(username)
        assert res is mocked_get_connection.return_value.get_user.return_value
        # assert res is mocked_get_connection().get_user()
