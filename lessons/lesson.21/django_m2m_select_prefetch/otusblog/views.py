from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.select_related('author').prefetch_related('tags')
