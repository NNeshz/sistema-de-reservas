from django.urls import path, re_path, include
from .views import RegisterView, LoginView, UserView, LogoutView, UserDeleteView, update_user_view, UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

from .views import UserProfileView, login, logout, create_user, staff

urlpatterns = (
    path('user/login/'   , LoginView.as_view()),             #Post
    path('user/logout/'  , LogoutView.as_view()),            #Post
    path('user/create/'  , RegisterView.as_view()),          #Post
    path('user/profile/' , UserView.as_view()),              #Get
    path('user/delete/'  , UserDeleteView.as_view()),        #Delete
    re_path('user/update/'      , update_user_view),         #Put
    # re_path('staff-only/'     , staff),                    #Post
    
    path('', include(router.urls)),
    
    path('api/user/profile/', UserProfileView.as_view({'get':'get', 'put':'put', 'delete':'delete'})),
    re_path('api/user/logout/', logout),
    re_path('api/user/login/', login), 
    re_path('api/user/create/', create_user),
    re_path('api/staff/', staff),
)