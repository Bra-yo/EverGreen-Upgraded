from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import House

class PropertyTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='manager@example.com',
            password='testpass',
            is_manager=True
        )
        self.house = House.objects.create(
            name="Test Villa",
            price=5000000,
            specs="3 bedrooms, 2 bathrooms",
            created_by=self.user
        )

    def test_house_creation(self):
        self.assertEqual(str(self.house), "Test Villa")

    def test_services_view(self):
        response = self.client.get('/services/')
        self.assertContains(response, "Test Villa")
