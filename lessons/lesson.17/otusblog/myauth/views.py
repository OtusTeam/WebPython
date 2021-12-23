from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from myauth.forms import OtusUserCreateForm
from myauth.models import OtusUser


class UserCreate(CreateView):
    model = OtusUser
    form_class = OtusUserCreateForm
    success_url = reverse_lazy('posting:index')


def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('posting:index'))
    context = {
        'form': form,
    }
    return render(request, 'myauth/login.html', context)
