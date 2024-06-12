from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDetailView, CreateUserView, UpdateUserView, StaffOnlyView, TableViewSet, ReservationStateViewSet, MenuViewSet, ReservationViewSet, ReservationMenuViewSet
# from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r'tables', TableViewSet)
router.register(r'reservation-states', ReservationStateViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'reservation-menus', ReservationMenuViewSet)
# projects_router = NestedDefaultRouter(router, r'projects', lookup='project')
# projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(projects_router.urls)),
    path('staff-only/', StaffOnlyView.as_view(), name='staff-only'), 
    path('create-user/', CreateUserView.as_view(), name='register'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('user-detail/', UserDetailView.as_view(), name='user-detail'), 
]