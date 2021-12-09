from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from posting.forms import PostCreateForm
from posting.models import Article, Author


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class PostListView(PageTitleMixin, ListView):
    model = Article
    page_title = 'Post List'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(published_at__isnull=False)
    #     return qs


class PostDetailView(PageTitleMixin, DetailView):
    page_title = 'Post Detail'
    model = Article


class PostCreateView(PageTitleMixin, CreateView):
    page_title = 'Post Create'
    # template_name = ''
    model = Article
    # fields = '__all__'
    # fields = ('author', 'title', 'text')
    form_class = PostCreateForm
    success_url = reverse_lazy('posting:index')


class PostUpdateView(PageTitleMixin, UpdateView):
    page_title = 'Post Update'
    model = Article
    form_class = PostCreateForm
    success_url = reverse_lazy('posting:index')


def author_list(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'posting/author_list.html', context=context)
