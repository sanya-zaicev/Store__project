from django.urls import path

from users.views import auth_user, register, profile

urlpatterns = [
    path('authorizations/', auth_user, name='auth'),
    path('registrations/', register, name='reg'),
    path('profile/', profile, name='profile'),
]