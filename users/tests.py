from django.test import TestCase
from django.utils.timezone import now
from django.test.client import Client

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
        self.client = Client()
        self.superuser = CustomUser.objects.create_superuser('superuser', 'super@test.com',
                                                             'password')
        self.user = CustomUser.objects.create_user('user', 'user@mail.ru', 'password')

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
        """Проверяем, что у нового юзера изначально неактивирован аккаунт"""
        self.assertEqual(self.custom_user.is_active, False)

    def test_activation_key_in_str(self):
        """Проверяем что ключ активации находится в строке"""
        self.assertIn('', self.custom_user.activation_key)

    def test_activation_key_expires(self):
        """Проверяем, что время создания юзера не равно activation_key_expires"""
        self.assertNotEqual(now(), self.custom_user.activation_key_expires)

    def test_activation_key_expires_2(self):
        """Проверяем, что время создания юзера не равно activation_key_expires"""
        self.assertTrue(self.custom_user.is_activation_key_expired)

    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Пользователь', status_code=200)

        # данные пользователя
        self.client.login(username='user', password='password')

        # логинимся
        response = self.client.get('/users/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # главная после логина
        response = self.client.get('/')
        self.assertContains(response, 'Пользователь', status_code=200)
        self.assertEqual(response.context['user'], self.user)

    def test_users_urls(self):
        response = self.client.get(f'/users/profile/{self.user.slug}/')
        self.assertEqual(response.status_code, 200)
