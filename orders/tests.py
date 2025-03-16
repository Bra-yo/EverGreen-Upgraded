from msilib.schema import Property

from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse

from orders.models import Order
from users.models import UserProfile


class OrderTests(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_my_orders_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('my_orders'))
        self.assertEqual(response.status_code, 200)

def test_add_to_cart_creates_order(self):
    property = Property.objects.create(name="Test House", price=100000)
    self.client.login(username='testuser', password='testpass123')
    response = self.client.post(
        reverse('add_to_cart', args=[property.id]),
        follow=True
    )
    self.assertEqual(Order.objects.count(), 1)

def test_duplicate_order_prevention(self):
    property = Property.objects.create(name="Test House", price=100000)
    Order.objects.create(user=self.user, property=property, status='pending')
    self.client.login(username='testuser', password='testpass123')
    response = self.client.post(
        reverse('add_to_cart', args=[property.id]),
        follow=True
    )
    self.assertEqual(Order.objects.count(), 1)  # No duplicate created