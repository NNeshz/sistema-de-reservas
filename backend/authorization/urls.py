from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include

from .views import UserProfileView, login, logout, create_user, staff, send_staff_invitation, process_staff_invitation, UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = (    
    path('', include(router.urls)),
    re_path('user/login/', login), 
    re_path('user/logout/', logout),
    
    re_path('user/create/', create_user),
    path('user/profile/', UserProfileView.as_view({'get':'get', 'put':'put', 'delete':'delete'})),
    
    re_path('staff/', staff),
    
    path('send-invitation/', send_staff_invitation, name='send_staff_invitation'),
    path('invite/', process_staff_invitation, name='process_staff_invitation'),
)
