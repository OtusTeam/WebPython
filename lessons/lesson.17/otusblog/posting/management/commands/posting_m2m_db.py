import random

from django.core.management.base import BaseCommand

from myauth.models import OtusUser
from posting.models import Article, Author, ArticleTag


class Command(BaseCommand):

    def handle(self, *args, **options):
        articles = list(Article.objects.all())
        print(f'articles: {len(articles)}')

        article_tags = list(ArticleTag.objects.all())
        print(f'article tags: {len(article_tags)}')

        for _ in range(5):
            article = random.choice(articles)
            tags = random.choices(article_tags, k=random.randint(1, 3))
            for tag in tags:
                article.tag.add(tag)
            article.save()
            print(f'{article.id}: {article.tag.all()}')

