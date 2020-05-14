from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import SecretView

urlpatterns = [
    path('', SecretView.as_view()),
    path('token/', views.obtain_auth_token),

    path('jwt/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]