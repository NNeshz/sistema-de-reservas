from django.contrib import admin
from .models import Table, Menu, Reservation, ReservationMenu, ReservationState, Category, SubCategory, InviteToken, Carrito, CarritoItem

SECRET_TOKEN_KEY = '23hio20'

admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(Carrito)
admin.site.register(Category)
admin.site.register(CarritoItem)
admin.site.register(SubCategory)
admin.site.register(InviteToken)
admin.site.register(Reservation)
admin.site.register(ReservationMenu)
admin.site.register(ReservationState)
