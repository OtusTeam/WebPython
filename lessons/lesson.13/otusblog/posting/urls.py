from django.urls import path
from . import views

urlpatterns = [
    path('published/', views.articles_list),
    path('new/', views.ArticleListView.as_view()),
]
