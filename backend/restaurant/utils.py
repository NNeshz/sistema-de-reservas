from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .models import InviteToken

# Esta es la función correcta. Estoy testeando
def send_staff_invitation(user):
    token = InviteToken.objects.create(user=user)
    invite_url = settings.SITE_URL + reverse('process-invite', args=[str(token.token)])
    send_mail(
        'Staff Invitation',
        f'Click the link to become a staff member: {invite_url}',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
