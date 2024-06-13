from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LogoutView, 
    ProcessInviteView, 
    UserDetailView, 
    CreateUserView, 
    DeleteUserView, 
    UpdateUserView, 
    StaffOnlyView, 
    TableViewSet, 
    ReservationStateViewSet, 
    MenuViewSet, 
    ReservationViewSet, 
    ReservationMenuViewSet
)
# from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'reservation-states', ReservationStateViewSet, basename='reservation-state')
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'reservation-menus', ReservationMenuViewSet, basename='reservation-menus')
# projects_router = NestedDefaultRouter(router, r'projects', lookup='project')
# projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')

# from .utils import send_staff_invitation
from .views import email_form, send_email #Pruebas de envío de correos 

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(projects_router.urls)),
    path('staff-only/', StaffOnlyView.as_view(), name='staff-only'), 
    path('user/create/', CreateUserView.as_view(), name='user-create'),
    path('user/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('user/update/', UpdateUserView.as_view(), name='user-update'),
    path('user/detail/', UserDetailView.as_view(), name='user-detail'), 
    path('user/login/', TokenObtainPairView.as_view(), name='user-login'),   
    path('user/logout/', LogoutView.as_view(), name='user-logout'),  # Hay que enviarle el refresh token 
      
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  
    path('api/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    
    path('invite/<uuid:token>/', ProcessInviteView.as_view(), name='process-invite'),
    
    path('email-form/', email_form, name='email_form'),
    path('send/', send_email, name='send'),
]
""" LogOut -> EL usuario no puede volver a hacer refresh de su token pero no debería expirar su token de acceso de manera simultanea?

En el flujo típico de JWT, el token de acceso (access token) tiene una vida útil corta y el token de actualización (refresh token) tiene una vida útil más larga. Cuando el usuario cierra sesión (logout) y el token de actualización se invalida, el token de acceso sigue siendo válido hasta que expire. Esto es por diseño para minimizar la necesidad de invalidar manualmente el token de acceso.

Si quieres que el token de acceso se invalide inmediatamente cuando el usuario cierre sesión, necesitarías mantener una lista de tokens de acceso revocados y verificar esta lista en cada solicitud. Sin embargo, esto puede complicar el diseño y disminuir algunas ventajas de usar JWT (como la no necesidad de almacenamiento en el servidor para manejar tokens).
"""