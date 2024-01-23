from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import MyUser
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    template_name = 'userapp/register.html'
    model = MyUser
    form_class = RegistrationForm
    success_url = reverse_lazy('userapp:login')

    # return HttpResponseRedirect('/')


class AuthView(LoginView):
    template_name = 'userapp/login.html'
