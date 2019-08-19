from unittest import mock
import pytest

from database import number_of_users_in_database, number_of_users_in_database_2


@pytest.fixture
def engine_with_user(engine_with_table_users):
    engine_with_table_users.execute(
        'INSERT INTO users (username) VALUES ("otus");'
    )
    return engine_with_table_users


@pytest.fixture
def engine_with_n_users(request, engine_with_table_users):
    for i in range(request.param):
        engine_with_table_users.execute(
            'INSERT INTO users (username) VALUES ("?");',
            params=(f'user_{i}', ),
        )
    return engine_with_table_users


def test_number_of_users_in_database(engine_with_user):
    assert number_of_users_in_database(engine_with_user) == 1


@pytest.mark.parametrize(
    'engine_with_n_users, expected', [
        (1, 1),
        (2, 2),
        (3, 3),
    ],
    indirect=['engine_with_n_users'],
)
def test_n_users_in_database(engine_with_n_users, expected):
    assert number_of_users_in_database(engine_with_n_users) == expected


@mock.patch('database.get_engine', autospec=True)
def test_number_of_users_in_database_2(mocked_get_engine, engine_with_user):
    mocked_get_engine.return_value = engine_with_user
    # mocked_get_engine.side_effect = lambda a, b: '1' if a else b
    assert number_of_users_in_database_2() == 1
    mocked_get_engine.assert_called_once()
    mocked_get_engine.assert_called_once_with('config', 'qwerty1234567')
    mocked_get_engine.assert_has_calls([
        mock.call('config', 'qwerty1234567'),
    ])
    # mocked_get_engine.assert_not_called()
