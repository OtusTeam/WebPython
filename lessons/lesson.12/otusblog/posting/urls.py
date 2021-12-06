from django.urls import path
from django.views.generic import TemplateView

import posting.views as posting

app_name = 'posting'

urlpatterns = [
    path('',
         # posting.posts_list,
         posting.PostListView.as_view(),
         name='index'),
    path('post/detail/<int:pk>/',
         # posting.post_detail,
         posting.PostDetailView.as_view(),
         name='post_detail'),
    path('authors/', posting.author_list, name='authors'),

    # path('about/', posting.about, name='about'),
    path('about/',
         TemplateView.as_view(template_name='posting/about.html'),
         name='about'),
]
