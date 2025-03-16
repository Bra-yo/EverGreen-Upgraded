from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order
from properties.models import House

class PaymentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass'
        )
        self.house = House.objects.create(
            name="Test Villa",
            price=500000,
            created_by=self.user
        )
        self.order = Order.objects.create(
            user=self.user,
            house=self.house
        )

    def test_payment_flow(self):
        self.client.login(email='test@example.com', password='testpass')
        response = self.client.post(
            f'/payments/process/{self.order.id}/',
            {'method': 'mpesa', 'phone': '254712345678'}
        )
        self.assertRedirects(response, '/my-orders/')