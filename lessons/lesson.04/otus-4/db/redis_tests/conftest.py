from pytest import fixture


@fixture
def redis_connection():
    print('redis_connection')
