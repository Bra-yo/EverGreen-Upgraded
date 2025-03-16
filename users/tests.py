from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpass123',
            phone='254712345678'
        )
        self.assertEqual(str(user), 'test@example.com')

    def test_manager_creation(self):
        manager = User.objects.create_superuser(
            email='manager@example.com',
            username='manager',
            password='adminpass',
            phone='254700000000',
            is_manager=True
        )
        self.assertTrue(manager.is_manager)