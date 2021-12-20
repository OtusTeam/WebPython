from django.core.management import BaseCommand
from mixer.backend.django import mixer

# import mixer
from posting.models import Article


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass
        # # simple case
        # otus_user = mixer.blend(OtusUser)
        # print(otus_user, type(otus_user))
        # print(vars(otus_user))

        # author = mixer.blend(Author)
        # print(author)

        # article = mixer.blend(Article)
        # print(article)
        # print(vars(article))

        # define case
        # otus_user = mixer.blend(OtusUser, email='user1111@otus.local')
        # print(vars(otus_user))

        # author = mixer.blend(Author, email='user1@otus.ru')
        # print(author, author.email)

        # cycling
        # blog_users = mixer.cycle(4).blend(OtusUser)
        # for blog_user in blog_users:
        #     print(blog_user)

        # authors = mixer.cycle(5).blend(Author)
        # [print(author) for author in authors]
        #
        # articles = mixer.cycle(2).blend(Article)
        # [print(article) for article in articles]

        # define in cycling
        # blog_users = mixer.cycle(3).blend(
        #     OtusUser,
        #     last_name='Ivanov',
        #     username=mixer.MIX.first_name  # username = first_name
        # )
        # for blog_user in blog_users:
        #     print(vars(blog_user))

        # authors = mixer.cycle(5).blend(
        #     Author,
        #     first_name=mixer.sequence('Ivan', 'Boris')
        # )
        # for author in authors:
        #     print(vars(author))

        articles = mixer.cycle(3).blend(
            Article,
            title=(el for el in ('First time', 'Now', 'Go further'))
        )
        for article in articles:
            print(vars(article))
