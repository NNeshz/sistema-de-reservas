from django.urls import path
from .tests import ProcessPaymentView
urlpatterns = (
    path('process_payment/', ProcessPaymentView.as_view(), name='process_payment'),
    )