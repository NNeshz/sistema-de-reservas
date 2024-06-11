from django.db import models
from django.contrib.auth.models import User

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

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tables = models.ManyToManyField(Table)
    start_date = models.DateField()
    end_date = models.DateField()
    state = models.ForeignKey(ReservationState, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservación {self.id} - Usuario: {self.user.username}"

class ReservationMenu(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"Reservación {self.reservation.id} - Menú: {self.menu.name}"
