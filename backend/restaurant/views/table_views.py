from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from ..permissions import IsStaffOrReadOnly
from ..serializers import TableSerializer
from ..models import Table


class TableViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
