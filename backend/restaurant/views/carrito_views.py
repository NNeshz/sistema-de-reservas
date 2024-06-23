from rest_framework import viewsets, mixins
from ..serializers import CarritoSerializer, CarritoItemSerializer
from ..models import Carrito, CarritoItem
from authorization.views import get_user_from_token

#Está incompleto -> Hace falta validaciones 

#Esto es lo que necesita el usuario, el retrieve debe ser modificado ya que solo debe poder acceder a su información (Su Carrito)
(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet) 


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

  
#No creo que sea necesario una vista. Se puede trabajar con el serializador.      
class CarritoItemViewSet(viewsets.ModelViewSet):
    queryset = CarritoItem.objects.all()
    serializer_class = CarritoItemSerializer
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

           