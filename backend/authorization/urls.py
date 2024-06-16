from django.urls import re_path
from .views import login, logout, profile, register, delete_user, update_user, staff

urlpatterns = [
    re_path('user/login/'   , login),             #Post
    re_path('user/logout/'  , logout),            #Post
    re_path('user/create/'  , register),          #Post
    re_path('user/profile/' , profile),           #Get
    re_path('user/delete/'  , delete_user),       #Delete
    re_path('user/update/'  , update_user),       #Put
    re_path('staff-only/'   , staff),             #Post
]
