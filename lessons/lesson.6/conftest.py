import pytest


@pytest.fixture(scope='module')
def default_args():
    print('initing fixture default_args')
    return -10, 20, 30


@pytest.fixture
def default_expected_result(default_args):
    print('initing default_expected_result')
    return 3, -1
