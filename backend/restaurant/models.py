from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    chairs = models.PositiveSmallIntegerField(default=1)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.id} - Capacidad: {self.chairs}"

class Category(models.Model):#Bebidas, Alimentos, Etc.
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model): #Bebidas calientes, Bebidas Frías, Sopas, Ensaladas, etc
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField('Imagen', upload_to='images/', max_length=255, null=True, blank=True)
    available = models.BooleanField(default=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}"

class CarritoItem(models.Model): 
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)
    
    def __str__(self):
        return f"{self.carrito.user}: {self.amount} {self.menu.name}"
