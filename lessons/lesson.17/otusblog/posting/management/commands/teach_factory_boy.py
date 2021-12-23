import factory.fuzzy
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory

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
    status = factory.fuzzy.FuzzyChoice(
        [el[0] for el in Author.STATUS_CHOICES]
    )
    bio = factory.Faker('paragraph')


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    author = factory.SubFactory(AuthorFactory)
    status = factory.fuzzy.FuzzyChoice(
        [el[0] for el in Article.STATUSES]
    )
    title = factory.Faker('sentence')
    text = factory.Faker('text')
    read_qty = factory.fuzzy.FuzzyInteger(0, 15)


def example_1():
    # articles = ArticleFactory.build_batch(5)
    articles = ArticleFactory.build_batch(
        5,
        # title=factory.Iterator(['New Year', 'New Django', 'New Ideas'])
        title=factory.Sequence(lambda n: f'Article {n}')
    )
    for article in articles:
        print(vars(article))


class Command(BaseCommand):

    def handle(self, *args, **options):
        example_1()
