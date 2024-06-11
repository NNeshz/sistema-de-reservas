from django.contrib import admin
from .models import Table, Menu, Reservation, ReservationMenu, ReservationState

admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(Reservation)
admin.site.register(ReservationMenu)
admin.site.register(ReservationState)