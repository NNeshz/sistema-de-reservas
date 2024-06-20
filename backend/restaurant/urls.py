from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from .views.reservation_views import (
    ReservationStateViewSet, 
    ReservationMenuViewSet,
    ReservationViewSet,
    ProcessInviteView, 
)
from .views.table_views import TableViewSet
from .views.menu_views import MenuViewSet
from .views.categories_views import CategoryView, SubCategoryView

router = DefaultRouter()

#Está funcionando perfectamente
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'menus', MenuViewSet, basename='menus')

#No testeado
router.register(r'category', CategoryView, basename='category')
router.register(r'subcategory', SubCategoryView, basename='subcategory')
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'reservation-states', ReservationStateViewSet, basename='reservation-state')
router.register(r'reservation-menus', ReservationMenuViewSet, basename='reservation-menus')

#En progreso
reservations_router = NestedDefaultRouter(router, r'reservations', lookup='reservations')
# reservations_router.register(r'menus', MenuView, basename='reservations-menus')
# reservations_router.register(r'tables', MenuViewSet, basename='reservations-tables')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(reservations_router.urls)),


    re_path('invite/', ProcessInviteView, name='process-invite'),
    # path('email-form/', email_form, name='email_form'),
    # path('send/', send_email, name='send'),
]


# from .utils import send_staff_invitation
# from .views import email_form, send_email #Pruebas de envío de correos 
