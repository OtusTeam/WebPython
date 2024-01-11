from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'userapp'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
