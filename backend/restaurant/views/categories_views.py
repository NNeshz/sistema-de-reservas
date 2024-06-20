from rest_framework import generics, viewsets
from ..models import Category, SubCategory
from ..serializers import CategorySerializer, SubCategorySerializer

class CategoryView(viewsets.ModelViewSet): #generics porque solo quiero que sea visible, no modificable
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SubCategoryView(viewsets.ModelViewSet): #generics porque solo quiero que sea visible, no modificable
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

