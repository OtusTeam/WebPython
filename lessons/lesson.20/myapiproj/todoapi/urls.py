from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('todos', views.ToDoItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('example/', views.ExampleView.as_view()),
    path('secret-view/', views.SecretView.as_view()),
]
