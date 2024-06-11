from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nombre

class Table(models.Model):
    chairs = models.IntegerField()
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.id} - Capacidad: {self.chairs}"

class ReservationState(models.Model):
    state = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.state

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Reservacion(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tables = models.ManyToManyField(Table, through='ReservationTable')
    start_date = models.DateField()
    end_date = models.DateField()
    id_state = models.ForeignKey(ReservationState, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservación {self.id} - Usuario: {self.id_user.name}"

class ReservationMenu(models.Model):
    id_reservation = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"Reservación {self.id_reservation.id} - Menú: {self.id_menu.name}"

class ReservacionMesa(models.Model):
    id_reservation = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    id_table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservación {self.id_reservation.id} - Mesa {self.id_table.id}"
