# from conftest import otus_user


def test_init(otus_user):
    username, user = otus_user
    assert user.username, username


def test_str(otus_user):
    username, user = otus_user
    assert str(user) == username


def test_delete(otus_super_user):
    username, user = otus_super_user
    assert user.delete() == True
