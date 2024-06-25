from rest_framework.viewsets import GenericViewSet, ModelViewSet
from ..serializers import CarritoSerializer, CarritoItemSerializer
from ..models import Carrito, CarritoItem, Menu
# from authorization.serializers import UserSerializer

#Está incompleto -> Hace falta validaciones 

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from ..serializers import CarritoSerializer, CarritoItemSerializer

class UserCarrito (GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarritoSerializer 
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

    def get(self, request): 
        #Buscamos carrito y obtenemos datos
        carrito = get_object_or_404(Carrito, user=request.user)   
        carrito = CarritoSerializer(carrito).data
        #Buscamos items relacionados al carrito
        items   = CarritoItem.objects.filter(carrito=carrito['id'])
        items   = CarritoItemSerializer(items, many=True).data
        return Response({'Carrito':carrito, 'Items':items}, status.HTTP_200_OK)
    
    def put(self, request):
        #Lo principal es recibir los datos del frontend. Este debe ser una lista con el producto a agregar y la cantidad
        #Obtengo el carrito 
        #Uso el carrito para obtener los elementos anteriores dentro del carrito 
        
        # # products = request.data.get('products', None)
        # products = ((2, 1), (5, 1), (7, 2)) #ID de producto TESTEO 
        # if not products:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # print(f'{products = }')
        
        # carrito = get_object_or_404(Carrito, user=request.user)   
        # print(f'{carrito = }')
        
        # carrito_products = CarritoItem.objects.filter(carrito=carrito)
        # print(f'Carrito antes de cargar los productos: {carrito_products = }')
        
        
        # productos_a_agregar = Menu.objects.filter(id__in=products) #Agregar al carrito
        # print(f'Productos a agregar: {productos_a_agregar}')
        # d = {}
        # for producto in carrito_products:
        #     if producto in d:
        #         d[producto.menu.id] += producto.menu.amount
        #     else:
        #         d.setdefault(producto.menu.id, 1)
        
        # for menu in productos_a_agregar:
        #     if menu.id in d:
        #         d[menu.id] += menu.amount
        #     else:
        #         d.setdefault(menu.id, 1)
        
        # print() 
        # print(f'{d = }')
        # print()
        # # CarritoItem.objects.create(carrito=carrito, menu=producto)
        
        # carrito_products = CarritoItem.objects.filter(carrito=carrito)
        # print(f'Carrito DESPUÉS de cargar los productos: {carrito_products = }')
        
        # all_price = sum(p.menu.price for p in carrito_products)
        
        # print(all_price)
        # print('\n\n\n\n')
        
        return Response({'PUT not implemented':''})
    
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

           
