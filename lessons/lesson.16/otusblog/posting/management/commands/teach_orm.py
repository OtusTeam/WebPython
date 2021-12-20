from random import choice, choices, randint

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import Count, F, Q, Prefetch
from django.db.models.functions import Length

from posting.models import Article, Author, ArticleTag


def step_1():
    articles = Article.objects.all()
    # articles = Article.objects.filter(id__isnull=False)
    # articles_qty = len(articles)  # python level
    # articles_qty = articles.count()  # db level
    # articles_id = [el.pk for el in articles]  # python level
    articles_id = articles.values('pk', 'title')  # db level
    # articles_id = articles.values_list('pk', 'title')  # db level
    # articles_id = [el[0] for el in articles.values_list('pk')]
    # articles_id = articles.values_list('pk', flat=True)  # -> list()
    # articles_id = articles.values_list('pk', 'title', flat=True)
    print(articles_id)
    # articles_objs = articles.only('pk')
    # articles_objs = articles
    # articles_objs = articles.values_list('pk')
    # articles_objs = articles.only('pk', 'title')
    # articles_objs = articles.values_list('pk', 'title')
    # articles_objs = articles.defer('author_id', 'edited_at')
    # print([f'{el.pk} ({type(el)})' for el in articles_objs])
    # print([f'{el.pk} /{el.title}/ ({type(el)})' for el in articles_objs])
    print(connection.queries)


def step_2():
    articles = Article.objects.all()
    # result = articles.values('tag__name')
    # result = articles.values('tag__name').annotate(Count('tag'))  # db level
    result = articles.values('tag__name').annotate(tag_qty=Count('tag'))  # db level
    print(result)
    last_q = connection.queries[-1]
    print(last_q['sql'])


def step_3():
    articles = Article.objects.all()
    # result = articles.aggregate(Count('pk'))  # -> dict
    # result = articles.annotate(n_tags=Count('tag'))  # apply to row in QS
    result = articles.annotate(n_tags=Count('tag'),
                               t_len=Length('title'))  # apply to row in QS -> QS
    result = result.filter(t_len__lte=8)
    # result = articles.aggregate(n_articles=Count('pk'),
    #                             start_posting=Min('created_at'),
    #                             finish_posting=Max('created_at'))  # whole QS -> dict
    # print(result)
    print([f'{el.title} /{el.t_len}/: {el.n_tags}' for el in result])
    last_q = connection.queries[-1]
    print(last_q['sql'])


def step_4():
    article_ids = Article.objects.values_list('pk', flat=True)
    rnd_article = Article.objects.get(pk=choice(article_ids))  # db -> python
    rnd_article.read_qty += 1  # python
    # rnd_article.save()  # python -> db
    rnd_article.save(update_fields=['read_qty'])  # python -> db

    print(*[f'{num}: {el["sql"]}'
            for num, el in enumerate(connection.queries, 1)],
          sep='\n\n')


def step_5():
    article_ids = Article.objects.values_list('pk', flat=True)
    # rnd_article = Article.objects.get(pk=choice(article_ids))
    # rnd_article = Article.objects.filter(pk=choice(article_ids)).first()
    # rnd_article.read_qty = F('read_qty') + 1
    # rnd_article.save(update_fields=['read_qty'])
    # Article.objects.filter(pk=choice(article_ids)).update(
    #     read_qty=F('read_qty') + 1
    # )
    Article.objects.update(read_qty=F('read_qty') + 1)

    print(*[f'{num}: {el["sql"]}'
            for num, el in enumerate(connection.queries, 1)],
          sep='\n\n')


def step_6():
    article_ids = Article.objects.values_list('pk', flat=True)
    rnd_articles = Article.objects.filter(pk__in=choices(article_ids, k=5))
    for article in rnd_articles:
        article.read_qty = F('read_qty') + randint(1, 10)
        # article.save(update_fields=['read_qty'])
    Article.objects.bulk_update(rnd_articles, fields=['read_qty'])
    # bulk_create

    print(*[f'{num}: {el["sql"]}'
            for num, el in enumerate(connection.queries, 1)],
          sep='\n\n')


def step_7():
    articles = Article.objects.annotate(n_tags=Count('tag'), t_len=Length('title'))
    # qs_1 = articles.filter(n_tags__gte=1)
    # qs_2 = articles.filter(t_len__lt=5)
    # qs_3 = qs_1.union(qs_2)  # +db level
    # print(qs_3)
    # qs_4 = articles.filter(Q(n_tags__gte=1) | ~Q(t_len__lt=5))
    # qs_4 = articles.filter(Q(n_tags__gte=1) & Q(t_len__lt=5))
    # qs_5 = articles.filter(n_tags__gte=1, t_len__lt=5)
    cond_1 = Q(n_tags__gte=1)
    cond_2 = Q(t_len__lt=5)
    qs_4 = articles.filter(cond_1 | cond_2)
    print(qs_4)

    # print(*[f'{num}: {el["sql"]}'
    #         for num, el in enumerate(connection.queries, 1)],
    #       sep='\n\n')


def step_8():
    articles = Article.objects.all()
    # articles_pks = [el.pk for el in articles]
    # articles_pks = [el.title for el in articles]  # ORM cache (python level)

    articles_pks = [el.pk for el in articles.iterator()]  # no ORM cache
    articles_pks = [el.title for el in articles]

    print(len(connection.queries))


def step_9():
    author = Author.objects.get(pk=1)
    # print(author.some_method())  # author.some_method
    # print(author.some_method())

    print(author.some_method)  # author.some_method
    print(author.some_method)

    print(len(connection.queries))


def step_10():
    initial_q_cnt = len(connection.queries)
    # articles = Article.objects.all()
    # articles = Article.objects.prefetch_related('tag').all()
    articles = Article.objects.prefetch_related(
        Prefetch('tag', queryset=ArticleTag.objects.filter(name__startswith='Гн'), to_attr='tags'),
        # Prefetch('tag', queryset=ArticleTag.objects.filter(name__startswith='Гн')),
    ).all()
    tags = []
    for item in articles:
        # _tags = item.tag.all()
        _tags = item.tags
        # _tags = item.tag.filter(name__startswith='Гн')
        print(_tags)
        tags.append(len(_tags))
        # tags.append(_tags)
    final_q_cnt = len(connection.queries)
    print(f'queries: {final_q_cnt - initial_q_cnt}, {len(tags)} records processed')


class Command(BaseCommand):

    def handle(self, *args, **options):
        # step_1()
        # step_2()
        # step_3()
        # step_4()
        # step_5()
        # step_6()
        # step_7()
        # step_8()
        # step_9()
        step_10()
