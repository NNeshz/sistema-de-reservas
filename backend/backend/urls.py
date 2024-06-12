from django.contrib import admin
from django.urls import path, include
from restaurant.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),    
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('', include('restaurant.urls')),
]

    # path('api-auth/', include('rest_framework.urls')),