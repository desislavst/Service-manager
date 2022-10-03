from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
import django.views.generic as views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from service_manager.accounts.forms import RegisterForm, LoginForm


class RegisterView(views.CreateView):
    form_class = RegisterForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('index')


class LoginUserView(auth_views.LoginView):
    template_name = 'login_user.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        return reverse_lazy('index')


class LogoutUserView(auth_views.LogoutView):
    pass
