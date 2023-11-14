from unittest import mock

from db_helper import get_user, User


# @mock.patch("db_helper.get_connection", spec=True)
@mock.patch("db_helper.get_connection")
def test_get_user(mocked_get_connection, otus_user):
    username, user = otus_user

    mocker_conn = mocked_get_connection.return_value
    mocked_conn_get_user = mocker_conn.get_user
    mocked_conn_get_user.return_value = user

    res = get_user(username)

    mocked_conn_get_user.assert_called()

    assert isinstance(res, User)
    assert res.username == user.username


    mocked_conn_get_user.assert_called_once()
    mocked_conn_get_user.assert_called_once_with(username)

    mocked_get_connection.assert_called_once()
    mocked_get_connection.assert_called_once_with()
