from .views import CustomTokenObtainPairView, UsersListView, UserProfileView, UserCreateView, SendStaffInvitationView, ProcessStaffInvitationView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = (
    path('user/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), #Login
    path('user/logout/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('user/create/', UserCreateView.as_view(), name='user'),
    path('user/profile/', UserProfileView.as_view(), name='user'),
    path('staff/', UsersListView.as_view(), name='users'),
    
    path('send-invitation/', SendStaffInvitationView.as_view(), name='send_staff_invitation'),
    path('invite/', ProcessStaffInvitationView.as_view(), name='process_staff_invitation'),
)
