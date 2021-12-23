import pytest

from myauth.models import OtusUser
from posting.models import Author


@pytest.fixture
def get_user_1():
    obj = OtusUser.objects.create_user('user_1',
                                       'user_1@otus.local',
                                       'OtusOtus')
    return obj


@pytest.mark.django_db
def test_1_author_create(get_user_1):
    obj = Author.objects.create(user=get_user_1,
                                status=Author.STATUS_JR,
                                bio='Some author 1')
    # print('user_1', vars(obj))
    assert obj.user.username == get_user_1.username
