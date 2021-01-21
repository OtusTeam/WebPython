from django.urls import path, include
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

urlpatterns = [
    path('token/', token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),
]
