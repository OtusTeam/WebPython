from typing import List

from django.core.management import BaseCommand
from mixer.backend.django import mixer

from otusblog.models import Tag, Author, Article


def create_tags():
    return [mixer.blend(Tag) for i in range(10)]


def create_articles(tags: List[Tag]):
    """
    :param tags:
    :return:
    """
    # a = mixer.blend(Author)

    article: Article = mixer.blend(Article, author__first_name='Ann')
    article.tags.set(tags)


class Command(BaseCommand):
    help = 'Using mixer. Creates Tag, Author and Article fixtures, deletes existing'

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        tags = create_tags()
        # Author.objects.all().delete()
        Article.objects.all().delete()
        create_articles(tags)
        print('Done!')
