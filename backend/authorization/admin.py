from django.contrib import admin
from.models import InviteToken

SECRET_TOKEN_KEY = '23hio20'

admin.site.register(InviteToken)