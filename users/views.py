from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomUserForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = CustomUserForm

    def get_success_url(self):
        return reverse('login')

class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("yaziki:yaizki_programmirovanie")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')

