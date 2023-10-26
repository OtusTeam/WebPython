from django.urls import path

from .views import (
    ShopAppIndexView,
    CategoriesListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryDeleteView,
)

app_name = "shop_app"

urlpatterns = [
    path("", ShopAppIndexView.as_view(), name="index"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category"),
    path("categories/<int:pk>/cofirm-delete/", CategoryDeleteView.as_view(), name="category-delete"),
]
