from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from .models import Menu, Table, User, Category, SubCategory, Carrito, CarritoItem

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'required': False}
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)
    
class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'chairs', 'price', 'description']

class MenuSerializer(ModelSerializer):
    """
    {
        "id": 1,
        "name": "Salmón",
        "description": "Salmón",
        "price": 50.0,
        "available": true,
        "subcategory": 5,
        "subcategory_name": "Pescado",
        "image": "http://localhost:8000/media/images/download_LxX1dJb.jpg"
    }
    """
    subcategory = PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    subcategory_name = StringRelatedField(source='subcategory.name', read_only=True)
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price', 'available', 'subcategory', 'subcategory_name', 'image']

class SubCategorySerializer(ModelSerializer):
    '''
    {
      { 'id': 1, 'name': 'Coca Cola', 'category': 1, 'category_name': 'Bebidas' },
      {
            "id": 1,
            "name": "Bebidas Frías",
            "category": 1,
            "category_name": "Bebidas"
        }
    }
    '''
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = StringRelatedField(source='category.name', read_only=True)


    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'category_name']
    
class SubCategoryDetailSerializer(ModelSerializer):
    '''
    {
      { 'id': 1, 'name': 'Coca Cola', 'category': 1, 'category_name': 'Bebidas' },
      {
            "id": 1,
            "name": "Bebidas Frías",
            "category": 1,
            "category_name": "Bebidas",
            "menus": [
                
                { "id": 1, "name": "Café Helado", "description": "Café frío con hielo."},
                { "id": 2, "name": "Limonada"   , "description": "Limonada fresca."    }
            ]
        }
    }
    '''
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = StringRelatedField(source='category.name', read_only=True)
    menus = MenuSerializer(source='menu_set', many=True, read_only=True) 


    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'category_name', 'menus']
    
class CategorySerializer(ModelSerializer):
    '''
    {
        {'id':1 , 'name':'Bebidas'}
        {'id':2 , 'name':'Alimentos'}
    }
    '''
    subcategory = SubCategorySerializer(source='subcategory_set', many=True, read_only=True) 
    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategory']

class CarritoSerializer(ModelSerializer):
    '''
    {
        "id": 1,
        "user": 1
    }
    '''
    
    class Meta:
        model = Carrito
        fields = '__all__'
        
class CarritoItemSerializer(ModelSerializer):
    '''
    [
        {
            "menu": "Ensalada Rusa",
            "amount": 1
        },
        {
            "menu": "Salmón",
            "amount": 2
        }
    ]
    '''
    
    menu = StringRelatedField(source='menu.name', read_only=True)
    
    class Meta:
        model = CarritoItem
        exclude = ('carrito', 'id')
        
