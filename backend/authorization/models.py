from django.db import models
from django.contrib.auth.models import User
import uuid

class InviteToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return str(self.token)