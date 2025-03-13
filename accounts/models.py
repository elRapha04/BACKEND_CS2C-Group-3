from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"  # Set email as the primary identifier
    REQUIRED_FIELDS = ["first_name", "last_name"]  # Required for user creation

    def __str__(self):
        return self.email
