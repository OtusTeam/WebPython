from pytest import fixture

from db_helper import User


# @fixture
@fixture(scope='module')
def otus_user():
    username = 'Otus'
    return username, User(username=username)
