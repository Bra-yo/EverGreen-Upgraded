from django.db import models

from orders.models import Order


class Payment(models.Model):
    PAYMENT_METHODS = [('mpesa', 'M-Pesa'), ('paypal', 'PayPal'), ('kcb', 'KCB'), ('equity', 'Equity')]
    order = models.OneToOneField(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='payment'  # Unique related name ✅
    )
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    STATUS_CHOICES = [
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

