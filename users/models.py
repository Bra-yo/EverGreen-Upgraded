from django.db import models

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    pass

    def __str__(self):
        return self.username

    # Add related_name arguments to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',  # Unique related_name
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Unique related_name
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username

class UserProfile(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_salesperson = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)
