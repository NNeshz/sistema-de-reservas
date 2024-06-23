from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField, StringRelatedField
from .models import Menu, Reservation, ReservationMenu, ReservationState, Table, User, Category, SubCategory, Carrito, CarritoItem

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

class ReservationStateSerializer(ModelSerializer):
    class Meta:
        model = ReservationState
        fields = ['id', 'state']

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
    
class ReservationSerializer(ModelSerializer): #Retorna las mesas, los menús y el estado vinculado a la reserva especifica del usuario 
    user = PrimaryKeyRelatedField(read_only=True)  # Solo lectura
    tables = PrimaryKeyRelatedField(queryset=Table.objects.all(), many=True)
    state = PrimaryKeyRelatedField(queryset=ReservationState.objects.all())
    menus = SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'tables', 'start_date', 'end_date', 'state', 'created_at', 'menus']

    def get_menus(self, obj):
        reservation_menus = ReservationMenu.objects.filter(reservation=obj)
        return MenuSerializer(reservation_menus, many=True).data
  
    def create(self, validated_data):
        tables_data = validated_data.pop('tables')
        reservation = Reservation.objects.create(**validated_data)
        reservation.tables.set(tables_data)
        return reservation
    
class ReservationMenuSerializer(ModelSerializer):
    class Meta:
        model = ReservationMenu
        fields = ['id', 'reservation', 'menu', 'amount']
        
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
        