from django.urls import path
from rest_framework.authtoken import views

from .views import HelloView

urlpatterns = [
    path('', HelloView.as_view()),
    path('token/', views.obtain_auth_token),
]
