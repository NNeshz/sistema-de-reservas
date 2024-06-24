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
from .views.categories_views import CategoryView, MenusSubCategoryRetrieveUpdateDestroyAPIView, SubCategoryView
from .views.carrito_views import CarritoViewSet, CarritoItemViewSet, UserCarrito

from django.conf import settings
from django.views.static import serve

router = DefaultRouter()

#Está funcionando perfectamente
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'menus', MenuViewSet, basename='menus')

#No testeado
router.register(r'category', CategoryView, basename='category')
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'carrito', CarritoViewSet) #RECIÉN AÑADIDO


# router.register(r'subcategory', MenusSubCategoryRetrieveUpdateDestroyAPIView)

router.register(r'reservation-states', ReservationStateViewSet, basename='reservation-state')
router.register(r'reservation-menus', ReservationMenuViewSet, basename='reservation-menus')

#En progreso
reservations_router = NestedDefaultRouter(router, r'reservations', lookup='reservations')
# reservations_router.register(r'menus', MenuView, basename='reservations-menus')
# reservations_router.register(r'tables', MenuViewSet, basename='reservations-tables')

carrito_items_router = NestedDefaultRouter(router, r'carrito', lookup='carrito_items') #RECIÉN AÑADIDO
carrito_items_router.register(r'elementos',CarritoItemViewSet, basename='carrito-items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(reservations_router.urls)),   
    path('', include(carrito_items_router.urls)),   
    path('subcategory/', SubCategoryView.as_view(), name='hola'),
    path('subcategory/<pk>/', MenusSubCategoryRetrieveUpdateDestroyAPIView.as_view(), name='subcategory-menus'),

    path('api/user/carrito/', UserCarrito.as_view({'get':'get', 'put':'put'})),

    re_path('invite/', ProcessInviteView, name='process-invite'),
    # path('email-form/', email_form, name='email_form'),
    # path('send/', send_email, name='send'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
] 


# from .utils import send_staff_invitation
# from .views import email_form, send_email #Pruebas de envío de correos 
