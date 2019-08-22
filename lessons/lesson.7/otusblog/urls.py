from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'otusblog'
urlpatterns = [
    # path('', views.index_view, name='index'),
    path('', views.IndexPageView.as_view(), name='index'),
    # path('', TemplateView.as_view(template_name='otusblog/index.html'), name='index'),
]
