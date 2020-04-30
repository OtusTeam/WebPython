from django.urls import path, include

# from .views import ToDoItemListView, ToDoItemDetailView
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, ToDoItemViewSet

router = DefaultRouter()
router.register('todo', ToDoItemViewSet)
router.register('author', AuthorViewSet)


# app_name = 'todoapi'

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/todo', ToDoItemListView.as_view()),
    # path('api/todo/<int:pk>', ToDoItemDetailView.as_view()),
]
