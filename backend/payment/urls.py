from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_preference, name='create_preference'),
    path('success/', views.payment_success, name='payment_success'),
    path('failure/', views.payment_failure, name='payment_failure'),
    path('pending/', views.payment_pending, name='payment_pending'),
]

