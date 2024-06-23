from rest_framework import generics, viewsets
from ..models import Category, SubCategory
from ..serializers import CategorySerializer, SubCategorySerializer, SubCategoryDetailSerializer

class CategoryView(viewsets.ModelViewSet): #generics porque solo quiero que sea visible, no modificable
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SubCategoryView(generics.CreateAPIView, generics.ListAPIView): #generics porque solo quiero que sea visible, no modificable
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

class MenusSubCategoryRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):#class MenusSubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubCategoryDetailSerializer
    queryset = SubCategory.objects.all()
    