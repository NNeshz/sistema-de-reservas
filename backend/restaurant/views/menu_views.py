from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from ..permissions import IsStaffOrReadOnly
from ..serializers import MenuSerializer
from ..models import Menu
"""
#localhost://reservations/2/menus/
#Al utilizar NestedDefaultRouter -> Debo trabajar con self.kwargs 

class MenuUserViewSet(viewsets.ModelViewSet): #No hay que permitir que el usuario cree o midifique menus
    serializer_class = ReservationMenuSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self): 
        return ReservationMenu.objects.filter(reservation=self.kwargs['reservations_pk'])
"""

class MenuViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

           
#http://localhost:8000/menus/         
# @api_view(['POST','PUT','DELETE','GET']) 
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])       
# def MenuViewSet(request):
    
#     if request.method == 'GET':
#         menus = Menu.objects.all()
#         serializer = MenuSerializer(menus, many=True)
#         return Response(serializer.data)
                
#     elif request.method == 'POST':
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

