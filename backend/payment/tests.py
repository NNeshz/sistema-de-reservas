from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.settings import MERCADOPAGO_ACCESS_TOKEN
import mercadopago
from restaurant.models import Menu
from django.http import JsonResponse
from rest_framework.decorators import api_view
import mercadopago
    
from rest_framework.renderers import TemplateHTMLRenderer

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        # Código de la vista aquí
        return Response()
    
sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

@api_view(['POST'])
def create_preference(request):
    print(f'\n{request.data}\n')
    preference_data = {
        "items": [
            {
                "title": request.data['description'],
                "unit_price": float(request.data['price']),
                "quantity": int(request.data['quantity']),
                'currency_id':'ARS'
            }
        ],
        "back_urls": {
            "success": "http://localhost:8000/feedback",
            "failure": "http://localhost:8000/feedback",
            "pending": "http://localhost:8000/feedback"
        },
        "auto_return": "approved",
        'binary_mode':False,
        'statement_descriptor': 'MININEGOCIO',
        'expires': False,
        'external_reference':'HOLAAAA_123'
    }
    response = sdk.preference().create(preference_data)

    return Response({'id':response['response']}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def feedback(request):
    return JsonResponse({
        'Payment': request.GET.get('payment_id'),
        'Status': request.GET.get('status'),
        'MerchantOrder': request.GET.get('merchant_order_id')
    })

# class ProcessPaymentView(APIView):
#     def post (self, request, *args, **kwargs):
#         print('Entró en post')
       
#     def put(self, request, *args, **kwargs): #POST
#         print('Entró en post')
        
#         data = request.data       
#         sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)
        
#         products, amount = [(id, amount) for id, amount in Menu. data.get('products')]
#         transaction_amount = sum(product.price for product in Menu.objects.filter(id__in=products))
        
#         return Response({
#             'transaction_amount':f'{transaction_amount = }',
#             'amount':f'{amount = }',
#             'data':f'{data = }',
#             'sdk':f'{sdk = }'}, status=status.HTTP_100_CONTINUE)
        
#         # payment_data = {
#         #     "transaction_amount": data['amount'],
#         #     "token": data['token'],
#         #     "description": "Pago de ejemplo",
#         #     "installments": int(data['installments']),
#         #     "payment_method_id": data['paymentMethodId'],
#         #     "payer": {
#         #         "email": data['payer']['email'],
#         #         "identification": {
#         #             "type": data['payer']['identification']['type'],
#         #             "number": data['payer']['identification']['number']
#         #         }
#         #     }
#         # }
        
#         # Payment de testeo -> Payment de teste -> Payment de testeo -> Payment de testeo
#         payment_data = {
#             "transaction_amount": 1000,  # Monto en centavos (10.00 ARS)
#             "token": "abc123xyz456",  # Token generado por el frontend
#             "description": "Pago de ejemplo",
#             "installments": 1,  # Número de cuotas
#             "payment_method_id": "visa",  # Método de pago (por ejemplo, 'visa')
#             "payer": {
#                 "email": "example@example.com",
#                 "identification": {
#                     "type": "DNI",  # Tipo de identificación (por ejemplo, 'DNI')
#                     "number": "12345678"  # Número de identificación
#                 }
#             }
#         }

#         payment_response = sdk.payment().create(payment_data)
#         payment = payment_response["response"]

#         if payment["status"] in ["approved", "in_process", "pending"]:
#             return Response({'success': True, 'message': 'Pago realizado con éxito!'}, status=status.HTTP_200_OK)

#         return Response({'success': False, 'message': f'{payment.get('status_detail', 'not detail')}'}, status=status.HTTP_400_BAD_REQUEST)


#Ejemplo 1
payment_data = {
    "transaction_amount": 1000,  # Monto en centavos (10.00 ARS)
    "token": "abc123xyz456",  # Token generado por el frontend
    "description": "Pago de ejemplo",
    "installments": 1,  # Número de cuotas
    "payment_method_id": "visa",  # Método de pago (por ejemplo, 'visa')
    "payer": {
        "email": "example@example.com",
        "identification": {
            "type": "DNI",  # Tipo de identificación (por ejemplo, 'DNI')
            "number": "12345678"  # Número de identificación
        }
    }
}

#Ejemplo 2
payment_data = {
    "transaction_amount": 1000,  # Monto en centavos (10.00 ARS)
    "description": "Pago de ejemplo",
    "payment_method_id": "account_money",  # Método de pago con cuenta de Mercado Pago
    "payer": {
        "email": "example@example.com",
        "identification": {
            "type": "DNI",  # Tipo de identificación (por ejemplo, 'DNI')
            "number": "12345678"  # Número de identificación
        }
    }
}


class CreatePreferenceView(APIView):
    def post(self, request, *args, **kwargs):
        # sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

        # Ejemplo de los datos de la preferencia
        preference_data = {
            "items": [
                {
                    "title": "Pago de ejemplo",
                    "quantity": 1,
                    "unit_price": 100.00
                }
            ],
            "payer": {
                "email": request.data.get('email')
            },
            "back_urls": {
                "success": "https://www.tu-sitio.com/success",
                "failure": "https://www.tu-sitio.com/failure",
                "pending": "https://www.tu-sitio.com/pending"
            },
            "auto_return": "approved"
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

        return Response({'preference_id': preference['id']}, status=status.HTTP_200_OK)