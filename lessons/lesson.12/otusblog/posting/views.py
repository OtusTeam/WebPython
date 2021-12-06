from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from posting.models import Article, Author


# # FBV
# def posts_list(request):
#     context = {
#         'posts': Article.objects.all(),
#     }
#     return render(request, 'posting/posts_list.html', context=context)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class PostListView(PageTitleMixin, ListView):
    model = Article
    page_title = 'Post List'

    # @method_decorator()
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch()

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(published_at__isnull=False)
        return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['page_title'] = 'Post List'
    #     return context


# def post_detail(request, post_pk):
#     # try:
#     #     article = Article.objects.get(pk=post_pk)
#     # except ...
#     # article = Article.objects.filter(pk=post_pk).first()
#     article = get_object_or_404(Article, pk=post_pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'posting/post_detail.html', context)


class PostDetailView(PageTitleMixin, DetailView):
    model = Article
    page_title = 'Post Detail'

    # template_name = 'posting/post_detail.html'
    # context_object_name = 'some_post'
    # pk_url_kwarg = 'post_pk'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['page_title'] = 'Post Detail'
    #     return context


def author_list(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'posting/author_list.html', context=context)

# def about(request):
#     return render(request, 'posting/about.html')
