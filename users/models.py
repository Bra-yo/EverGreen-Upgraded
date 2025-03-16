from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_salesperson = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)

    # Fix permission clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email  # More useful than username