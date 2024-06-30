from django.http import JsonResponse
from django.shortcuts import render
# from django.conf import settings
from backend.settings import MERCADOPAGO_ACCESS_TOKEN
import mercadopago



def create_preference(request):
    if request.method == 'POST':
        sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

        preference_data = {
            "items": [
                {
                    "title": 'Libro',
                    "quantity": 1,
                    "unit_price": float(5)
                }
            ],
            "back_urls": {
                "success": request.build_absolute_uri('/payments/success/'),
                "failure": request.build_absolute_uri('/payments/failure/'),
                "pending": request.build_absolute_uri('/payments/pending/')
            },
            "auto_return": "approved"
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

        print('\n\n',preference,'\n\n')

        return JsonResponse({'init_point': preference['sandbox_init_point']})

    if request.method == 'GET':
        return render(request, 'create_payment.html')

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_failure(request):
    return render(request, 'payments/failure.html')

def payment_pending(request):
    return render(request, 'payments/success.html')