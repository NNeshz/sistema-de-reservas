from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # LogoutView, 
    # ProcessInviteView, 
    # UserProfileView, 
    # CreateUserView, 
    # DeleteUserView, 
    # UpdateUserView, 
    # StaffOnlyView, 
    TableViewSet, 
    ReservationStateViewSet, 
    MenuViewSet, 
    ReservationViewSet, 
    ReservationMenuViewSet,
    # LogginView,
    MenuUserViewSet
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'reservation-states', ReservationStateViewSet, basename='reservation-state')
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'reservation-menus', ReservationMenuViewSet, basename='reservation-menus')

reservations_router = NestedDefaultRouter(router, r'reservations', lookup='reservations')
reservations_router.register(r'menus', MenuUserViewSet, basename='reservations-menus')
reservations_router.register(r'tables', MenuViewSet, basename='reservations-tables')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(reservations_router.urls)),
    #Retornan un json 
    # path('user/profile/', UserProfileView.as_view(), name='user-login'),   #Retorna infomación de usuario y cookie con token
    # path('user/login/', LogginView.as_view(), name='user-login'),  #Realiza autentificación, Retorna infomación de usuario, Cookie con token y sesion ID
    # path('user/create/', CreateUserView.as_view(), name='user-create'), #Retorna cookie con token 
    # path('user/delete/', DeleteUserView.as_view(), name='user-delete'), #Elimina correctamente el usuario
    # path('user/update/', UpdateUserView.as_view(), name='user-update'),
    
    # path('staff-only/', StaffOnlyView.as_view(), name='staff-only'), 
      
    # path('user/logout/', LogoutView.as_view(), name='user-logout'),  #Limpiar cookie (delete_cookie) # Hay que enviarle el refresh token 
    # path('user/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'), #Ya no es necesario.. Al llamar Profile, se hace un refresh del token 
    
    # path('invite/<uuid:token>/', ProcessInviteView.as_view(), name='process-invite'),
    # path('email-form/', email_form, name='email_form'),
    # path('send/', send_email, name='send'),
]


# from .utils import send_staff_invitation
# from .views import email_form, send_email #Pruebas de envío de correos 
