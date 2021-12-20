from django.urls import path

import myauth.views as myauth

app_name = 'myauth'

urlpatterns = [
    path('user/create/',
         myauth.UserCreate.as_view(),
         name='user_create'),
    path('user/login/',
         myauth.login,
         name='user_login'),
]
