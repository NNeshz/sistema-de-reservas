from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('', include('authorization.urls')),
]
# path('api-auth/', include('rest_framework.urls')),