from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from .models import CustomUser


class TestCustomUser(TestCase):

    def setUp(self):
        self.custom_user = CustomUser.objects.create(
            username='X',
            email='x@gmail.com',
            first_name='John',
            last_name='McGregor',
            password='123',
            phone='+71234567890'
        )

    def tearDown(self):
        del self.custom_user

    def test_create(self):
        """Проверяем, что поля модели соотв. нужным типам данных"""
        self.assertEqual(self.custom_user.username, 'X')
        self.assertEqual(self.custom_user.email, 'x@gmail.com')
        self.assertEqual(self.custom_user.first_name, 'John')
        self.assertEqual(self.custom_user.last_name, 'McGregor')
        self.assertEqual(self.custom_user.password, '123')
        self.assertEqual(self.custom_user.phone, '+71234567890')

    def test_user_is_active(self):
        """Проверям, что у нового юзера изначально неактивирован аккаунт"""
        self.assertEqual(self.custom_user.is_active, False)

    def test_activation_key_in_str(self):
        """Проверяем что ключ активации находится в строке"""
        self.assertIn('', self.custom_user.activation_key)

    def test_activation_key_expires(self):
        """Проверяем, что время создания юзера не равно activation_key_expires"""
        self.assertNotEqual(now(), self.custom_user.activation_key_expires)

    def test_activation_key_expires_2(self):
        """Проверяем, что время создания юзера не равно activation_key_expires"""
        self.assertTrue(self.custom_user.is_activation_key_expires())
