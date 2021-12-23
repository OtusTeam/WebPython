import random

from django.core.management.base import BaseCommand

from myauth.models import OtusUser
from posting.models import Article, Author, ArticleTag


class Command(BaseCommand):

    def handle(self, *args, **options):
        # users
        for num in range(1, 4):
            username = f'user_{num}'
            if not OtusUser.objects.filter(username=username).exists():
                OtusUser.objects.create_user(
                    username=username,
                    email=f'{username}@otus.local',
                    password='OtusOtus'
                )

        users = OtusUser.objects.all()
        print(f'users: {users.count()}')

        # authors
        for user in users:
            if not Author.objects.filter(user=user).exists():
                Author.objects.create(
                    user=user
                )
        authors = Author.objects.all()
        print(f'authors: {authors.count()}')

        # articles
        alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        alphabet.append(' ')
        authors_l = list(authors)
        for num in range(10):
            author = random.choice(authors_l)
            a_title = "".join(random.choice(alphabet)
                              for _ in range(random.randint(3, 15))).title()
            a_text = "".join(random.choice(alphabet)
                             for _ in range(random.randint(15, 50))).capitalize()
            Article.objects.create(
                author=author,
                title=a_title,
                text=a_text,
            )

        articles = Article.objects.all()
        print(f'articles: {articles.count()}')

        # tags
        for num in range(20):
            t_name = "".join(random.choice(alphabet)
                             for _ in range(random.randint(3, 10))).title()
            ArticleTag.objects.create(
                name=t_name
            )

        article_tags = ArticleTag.objects.all()
        print(f'article tags: {article_tags.count()}')
