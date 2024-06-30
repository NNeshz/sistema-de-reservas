from rest_framework import generics, viewsets
from ..models import Category, SubCategory
from ..serializers import CategorySerializer, SubCategorySerializer, SubCategoryDetailSerializer

from ..permissions import IsStaffOrReadOnly

class CategoryView(generics.ListAPIView): #generics porque solo quiero que sea visible, no modificable
    # permission_classes = [IsStaffOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SubCategoryView(generics.CreateAPIView, generics.ListAPIView): #generics porque solo quiero que sea visible, no modificable
    # permission_classes = [IsStaffOrReadOnly]
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

class MenusSubCategoryRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):#class MenusSubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    # permission_classes = [IsStaffOrReadOnly]
    serializer_class = SubCategoryDetailSerializer
    queryset = SubCategory.objects.all()
    