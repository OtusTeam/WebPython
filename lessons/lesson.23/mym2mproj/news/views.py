from django.views.generic import ListView

from .models import Article, Tag


class ArticleListView(ListView):
    template_name = "news/articles.html"
    queryset = Article.objects.select_related("author").prefetch_related("tags").all()


class TagListView(ListView):
    template_name = "news/tags.html"
    queryset = Tag.objects.prefetch_related("articles", "articles__author").all()
