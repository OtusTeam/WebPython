from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from myauth.forms import OtusUserCreateForm
from myauth.models import OtusUser


class UserCreate(CreateView):
    model = OtusUser
    form_class = OtusUserCreateForm
    success_url = reverse_lazy('posting:index')
