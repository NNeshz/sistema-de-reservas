from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, StaffOnlyView, UserViewSet, TableViewSet, ReservationStateViewSet, MenuViewSet, ReservationViewSet, ReservationMenuViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservation-states', ReservationStateViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'reservation-menus', ReservationMenuViewSet)
# router.register(r'staff-only', StaffOnlyView)

urlpatterns = [
    path('', include(router.urls)),
    path('staff-only/', StaffOnlyView.as_view(), name='staff-only'),  # Añadir StaffOnlyView directamente
    path('create-user/', CreateUserView.as_view(), name='register'),
]