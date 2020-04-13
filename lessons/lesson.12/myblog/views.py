from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Article

def index_view(request):
    # return HttpResponse('<h1>Hello django blog index!</h1>')
    article = Article.objects.get(pk=1)
    context = {
        'foo': 'bar',
        'spam': 'eggs',
        'article': article,
        'all_articles': Article.objects.all(),
        'all_j_authors': Author.objects.filter(first_name__startswith='J')
    }
    return render(request, 'myblog/index.html', context=context)
