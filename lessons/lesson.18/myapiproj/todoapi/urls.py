from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ToDoItemListView, ToDoItemDetailView, AuthorViewSet, ToDoItemViewSet


router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('todos', ToDoItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('todos/', ToDoItemListView.as_view()),
    # path('todos/<int:pk>/', ToDoItemDetailView.as_view()),
]
