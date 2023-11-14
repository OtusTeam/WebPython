from pytest import fixture

from db_helper import User


@fixture(scope='session', autouse=True)
def clear():
    print('prepare it')
    yield
    print('crear it')


@fixture(scope='session')
# @fixture
def otus_user():
    print('otus_user')
    username = 'Otus'
    return username, User(username=username)


@fixture
def otus_super_user():
    print('otus_super_user')
    username = 'SuperOtus'
    return username, User(username=username)
