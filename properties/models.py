from django.db import models
from django.conf import settings

class House(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.TextField()
    image = models.ImageField(upload_to='houses/')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='houses_created'
    )

    def __str__(self):
        return self.name