from django.urls import path, include

from rest_framework.routers import DefaultRouter
# from .views import ToDoItemListView, ToDoItemDetailView
from .views import AuthorViewSet, ToDoItemViewSet


router = DefaultRouter()
router.register("todos", ToDoItemViewSet)
router.register("authors", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("todos/", ToDoItemListView.as_view()),
    # path("todos/<int:pk>", ToDoItemDetailView.as_view()),
]
