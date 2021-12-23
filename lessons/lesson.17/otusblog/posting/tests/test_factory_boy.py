import factory
import pytest
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyInteger

from myauth.models import OtusUser
from posting.models import Author, Article


class OtusUserFactory(DjangoModelFactory):
    class Meta:
        model = OtusUser

    # username = factory.Faker('user_name')
    username = factory.LazyAttribute(lambda o: o.email.split('@')[0])
    # username = factory.SelfAttribute('email')
    email = factory.Faker('email')


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    user = factory.SubFactory(OtusUserFactory)
    status = FuzzyChoice([el[0] for el in Author.STATUS_CHOICES])
    bio = factory.Faker('paragraph')


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    author = factory.SubFactory(AuthorFactory)
    status = FuzzyChoice([el[0] for el in Article.STATUSES])
    title = factory.Faker('sentence')
    text = factory.Faker('text')
    read_qty = FuzzyInteger(0, 15)


@pytest.fixture
def get_user_2():
    # obj = OtusUserFactory.create(email='user_3@otus.local',
    #                              is_staff=True)
    obj = OtusUserFactory.create()
    # obj = OtusUserFactory.build()
    return obj


@pytest.mark.django_db
def test_2_author_create(get_user_2):
    obj = Author.objects.create(user=get_user_2,
                                status=Author.STATUS_MD,
                                bio='Some author 2')
    # print('user_2', vars(get_user_2))
    # print('author', vars(obj))
    assert obj.user.username == get_user_2.username


@pytest.mark.django_db
def test_3_author_create():
    # author = AuthorFactory.build()
    author = AuthorFactory.create()
    # print('user', vars(author.user))
    # print('author', vars(author))
    assert author.user.username is not None


@pytest.mark.django_db
def test_1_article_create():
    article = ArticleFactory.create()
    # print('user', vars(article.author.user))
    # print('article', vars(article))
    assert article.author.user.username is not None
