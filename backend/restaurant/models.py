from django.db import models
from django.contrib.auth.models import User
import uuid

class InviteToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

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
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100, unique=True)
    tables = models.ManyToManyField(Table)
    start_date = models.DateField()
    end_date = models.DateField()
    state = models.ForeignKey(ReservationState, on_delete=models.CASCADE) #Quizas podría hacerlo un campo de texto
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValueError ('The end date must be after the start date.')


    def __str__(self):
        return f"Reservación {self.id} - Usuario: {self.user.username}"

class ReservationMenu(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    amount = models.IntegerField() #Cantidad de platos 

    def __str__(self):
        return f"Reservación {self.reservation.id} - Menú: {self.menu.name}"
