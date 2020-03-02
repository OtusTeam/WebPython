import random
from typing import List
import factory

from faker import Faker
from django.core.management import BaseCommand

from otusblog.models import Tag, Author, Article

fake = Faker()


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Tag

    name = factory.Faker('word')


class AuthorFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    last_name = factory.LazyFunction(fake.last_name)


class ArticleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Article

    title = factory.Faker('sentence')
    body = factory.Faker('text')

    author = factory.SubFactory(AuthorFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        """
        :param create:
        :param extracted:
        :param kwargs:
        :return:
        """
        if not create:
            return

        if extracted:
            self.tags.set(extracted)
            # for tag in extracted:
            #     self.tags.add(tag)


def create_tags():
    tags = TagFactory.create_batch(10)
    return tags


def create_author():
    return AuthorFactory.create()


def create_article(tags: List[Tag], author: Author):
    """
    :param tags:
    :param author:
    :return:
    """
    some_tags = random.sample(tags, random.randint(1, len(tags)))
    article = ArticleFactory(author=author, tags=some_tags)
    # article = ArticleFactory(tags=some_tags)
    # article = ArticleFactory()
    # article.tags.set(tags)
    return article


def create_articles(tags: List[Tag]):
    """
    :param tags:
    :return:
    """
    # a = mixer.blend(Author)

    some_tags = random.sample(tags, random.randint(1, len(tags)))
    # articles = ArticleFactory.create_batch(3, tags=some_tags, author__last_name='Smith')
    articles = ArticleFactory.create_batch(70, tags=some_tags, author__last_name='Smith')
    return articles


class Command(BaseCommand):
    help = 'Using mixer. Creates Tag, Author and Article fixtures, deletes existing'

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        Article.objects.all().delete()
        Author.objects.all().delete()

        tags = create_tags()
        a = create_author()
        create_article(tags, a)
        create_articles(tags)
        print('Done!')
