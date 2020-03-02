from django.urls import path

from .views import ArticleListView

app_name = 'otusblog'

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
]
