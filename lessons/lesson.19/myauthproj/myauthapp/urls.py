from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    token_obtain_pair,
    token_refresh,
)

from .views import SecretView

urlpatterns = [
    path("", SecretView.as_view()),

    path("token/", views.obtain_auth_token),

    path('jwt-token/', token_obtain_pair, name='token_obtain_pair'),
    path('jwt-token/refresh/', token_refresh, name='token_refresh'),
]
