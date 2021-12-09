from django.urls import path
from django.views.generic import TemplateView

import posting.views as posting

app_name = 'posting'

urlpatterns = [
    path('',
         posting.PostListView.as_view(),
         name='index'),
    path('post/create/',
         posting.PostCreateView.as_view(),
         name='post_create'),
    path('post/update/<int:pk>/',
         posting.PostUpdateView.as_view(),
         name='post_update'),
    path('post/detail/<int:pk>/',
         posting.PostDetailView.as_view(),
         name='post_detail'),

    path('authors/', posting.author_list, name='authors'),

    path('about/',
         TemplateView.as_view(template_name='posting/about.html'),
         name='about'),
]
