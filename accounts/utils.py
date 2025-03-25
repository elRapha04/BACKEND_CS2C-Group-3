from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

def send_verification_email(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = f"http://127.0.0.1:8000/api/accounts/verify-email/{uid}/{token}/"

    subject = "Verify your email"
    message = f"Hi {user.first_name},\n\nPlease verify your email by clicking the link below:\n{verification_link}\n\nThank you!"
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
