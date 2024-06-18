from django.urls import path, re_path
from .views import RegisterView, LoginView, UserView, LogoutView, UserDeleteView, update_user_view

urlpatterns = [
    path('user/login/'   , LoginView.as_view()),             #Post
    path('user/logout/'  , LogoutView.as_view()),            #Post
    path('user/create/'  ,  RegisterView.as_view()),          #Post
    path('user/profile/' , UserView.as_view()),           #Get
    path('user/delete/'  , UserDeleteView.as_view()),       #Delete
    re_path('user/update/'  , update_user_view),       #Put
    # re_path('staff-only/'   , staff),             #Post
]