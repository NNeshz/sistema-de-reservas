from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TableViewSet, ReservationStateViewSet, MenuViewSet, ReservationViewSet, ReservationMenuViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservation-states', ReservationStateViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'reservation-menus', ReservationMenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]