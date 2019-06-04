from django.urls import path
# from django.views.generic import TemplateView

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index_view),
    # path('', TemplateView.as_view(template_name='todo/index.html'))
    path('api/todo/', views.ToDoListView.as_view()),
    path('api/todo/<int:pk>', views.ToDoDetailView.as_view()),
]
