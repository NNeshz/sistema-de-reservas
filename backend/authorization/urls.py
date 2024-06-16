# from django.contrib import admin
from django.urls import path, re_path

from .views import login, logout, profile, register, delete_user, update_user, staff

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path('login'   , login),             #Post
    re_path('logout'  , logout),            #Post
    re_path('register', register),          #Post
    re_path('profile' , profile),           #Get
    re_path('delete_user' , delete_user),   #Delete
    re_path('update_user' , update_user),   #Put
    re_path('staff'   , staff),             #Post
]
