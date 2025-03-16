
from django.db import models

from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'  # Unique related name ✅
    )
    house = models.ForeignKey(  # Rename from 'property' to 'house' ✅
        'properties.House',  # Match actual model name
        on_delete=models.CASCADE,
        related_name='orders'
    )


    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('delivered', 'Delivered')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'house'],
                condition=models.Q(status='pending'),
                name='unique_pending_order_per_property'
            )
        ]

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"