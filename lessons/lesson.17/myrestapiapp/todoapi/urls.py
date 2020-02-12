from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TodoItemListView, TodoItemDetailView, TodoItemViewSet, AuthorViewSet

router = DefaultRouter()
router.register('todo', TodoItemViewSet)
router.register('author', AuthorViewSet)


urlpatterns = [
    path('api/', include(router.urls))
    # path('api/todo/', TodoItemListView.as_view()),
    # path('api/todo/<int:pk>/', TodoItemDetailView.as_view()),
]
