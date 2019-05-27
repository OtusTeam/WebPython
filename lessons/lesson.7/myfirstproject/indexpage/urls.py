from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = 'indexpage'
urlpatterns = [
    # path('', views.index_page),
    path('', views.IndexPageView.as_view()),
    # path('', TemplateView.as_view(template_name='indexpage/index.html')),

]
