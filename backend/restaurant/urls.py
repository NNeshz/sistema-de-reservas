from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDetailView, CreateUserView, DeleteUserView, UpdateUserView, StaffOnlyView, TableViewSet, ReservationStateViewSet, MenuViewSet, ReservationViewSet, ReservationMenuViewSet
# from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'reservation-states', ReservationStateViewSet, basename='reservation-state')
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'reservation-menus', ReservationMenuViewSet, basename='reservation-menus')
# projects_router = NestedDefaultRouter(router, r'projects', lookup='project')
# projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(projects_router.urls)),
    path('staff-only/', StaffOnlyView.as_view(), name='staff-only'), 
    path('user/create/', CreateUserView.as_view(), name='user-create'),
    path('user/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('user/update/', UpdateUserView.as_view(), name='user-update'),
    path('user/detail/', UserDetailView.as_view(), name='user-detail'), 
    path('user/login/', TokenObtainPairView.as_view(), name='user-token'),    
    path('user/token/refresh/', TokenRefreshView.as_view(), name='user-token-refresh'),
]
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/token/', TokenObtainPairView.as_view(), name='user-token'),    
    path('user/token/refresh/', TokenRefreshView.as_view(), name='user-token-refresh'),
]
"""