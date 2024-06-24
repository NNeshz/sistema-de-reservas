from rest_framework.viewsets import GenericViewSet, ModelViewSet
from ..serializers import CarritoSerializer, CarritoItemSerializer
from ..models import Carrito, CarritoItem
from authorization.views import get_user_from_token
# from authorization.serializers import UserSerializer

#Está incompleto -> Hace falta validaciones 


from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class UserCarrito (GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    '''
    {
        "Carrito": {
            "id": 2,
            "user": 11
        },
        "Items": {   
            {
                "menu": "Ensalada Rusa",
                "amount": 1
            },
            {
                "menu": "Salmón",
                "amount": 2
            }
        }
    }
    '''
    def get(self, request):   #Aún no existe el carrito...
        #Buscamos carrito y obtenemos datos
        carrito = get_object_or_404(Carrito, user=request.user)   
        carrito = CarritoSerializer(carrito).data
        #Buscamos items relacionados al carrito
        items   = CarritoItem.objects.filter(carrito=carrito['id'])
        items   = CarritoItemSerializer(items, many=True).data
        return Response({'Carrito':carrito, 'Items':items}, status.HTTP_200_OK)
    
    def put(self, request):  
        return Response(status=status.HTTP_200_OK)
    


class CarritoViewSet(ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

#No creo que sea necesario una vista. Se puede trabajar con el serializador.      
class CarritoItemViewSet(ModelViewSet):
    queryset = CarritoItem.objects.all()
    serializer_class = CarritoItemSerializer
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

           