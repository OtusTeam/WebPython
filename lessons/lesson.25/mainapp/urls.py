from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('animal/list/', views.AnimalListView.as_view(), name='animal_list'),
    path('animal/create/', views.AnimalCreateView.as_view(), name='animal_create'),

    path('contact/', views.ContactFormView.as_view(), name='contact'),
]
