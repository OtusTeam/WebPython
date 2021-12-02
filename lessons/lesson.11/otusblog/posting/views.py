from django.shortcuts import render

from posting.models import Article


def posts_list(request):
    context = {
        'posts': Article.objects.all(),
    }
    return render(request, 'posting/posts_list.html', context=context)
