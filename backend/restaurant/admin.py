from django.contrib import admin
from .models import Table, Menu, Reservacion, ReservationMenu, ReservationState, ReservacionMesa

admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(Reservacion)
admin.site.register(ReservationMenu)
admin.site.register(ReservationState)
admin.site.register(ReservacionMesa)