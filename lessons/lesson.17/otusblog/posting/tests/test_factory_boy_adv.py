import factory
import pytest
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyInteger

from myauth.models import OtusUser
from posting.models import Author, Article


class OtusUserFactory(DjangoModelFactory):
    class Meta:
        model = OtusUser

    username = factory.LazyAttribute(lambda o: o.email.split('@')[0])
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
    # status = FuzzyChoice([el[0] for el in Article.STATUSES[:3]])
    status = FuzzyChoice(Article.STATUSES[:3], getter=lambda x: x[0])
    title = factory.Faker('sentence')
    text = factory.Faker('text')
    # read_qty = FuzzyInteger(0, 15)
    read_qty = 0

    class Params:
        published = factory.Trait(
            status=Article.PUBLISHED,
            read_qty=FuzzyInteger(0, 15)
        )


class PublishedArticleFactory(ArticleFactory):
    published = True


@pytest.mark.django_db
def test_not_published_article_create():
    article = ArticleFactory.create()
    print('not published article', vars(article))
    assert article.author.user.username is not None


@pytest.mark.django_db
def test_published_article_create():
    # article = ArticleFactory.create(published=True)
    article = PublishedArticleFactory.create()
    print('published article', vars(article))
    assert article.author.user.username is not None
