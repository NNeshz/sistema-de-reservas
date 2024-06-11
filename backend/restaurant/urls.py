from django.urls import path
from .views import login, register, profile
urlpatterns = [
    path('login', login),
    path('register', register),
    path('profile', profile),
    
    ]