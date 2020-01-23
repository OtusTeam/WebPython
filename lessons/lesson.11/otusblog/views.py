from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Article
from django.db.models import Q

def index_view(request):
    # return HttpResponse('<h1>Hello world!</h1>')
    args = {
        'foo': 'bar',
        'spam': 'eggs',
    }
    Author.objects.get(id=1)
    Author.objects.get(pk=2)
    Author.objects.filter(first_name='James')
    Author.objects.filter(first_name__startswith='J')
    james = Author.objects.get(first_name='James')
    Article.objects.filter(author=james)
    Author.objects.filter(first_name__startswith='J', last_name__endswith='n')
    Author.objects.filter(Q(first_name__startswith='J') | Q(last_name__endswith='n'))

    return render(request, 'otusblog/index.html', args)
