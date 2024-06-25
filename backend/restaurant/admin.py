from django.contrib import admin
from .models import Table, Menu, Category, SubCategory, Carrito, CarritoItem

admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(Carrito)
admin.site.register(Category)
admin.site.register(CarritoItem)
admin.site.register(SubCategory)
