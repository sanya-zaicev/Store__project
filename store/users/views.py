from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserAuthForm, UserRegistrationsForm, UserProfileForm
from users.models import User

class UserLoginView(LoginView):
    template_name = 'users/auth.html'
    form_class = UserAuthForm

    def get_success_url(self):
        return reverse_lazy('index')

class UserRegistrationsView(CreateView):
    model = User
    form_class = UserRegistrationsForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('auth')

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    def get_success_url(self):
        return reverse_lazy('profile', args=(self.request.user.id,))

