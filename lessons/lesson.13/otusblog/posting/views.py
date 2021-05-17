from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


def articles_list(request: HttpRequest):
    context = {
        "articles": Article.objects.filter(published_at__isnull=False)
    }
    return render(request, "posting/articles_list.html", context)


class ArticleListView(ListView):

    model = Article
    template_name = "posting/articles_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(published_at__isnull=False)

    def get_context_object_name(self, object_list):
        return "articles"
