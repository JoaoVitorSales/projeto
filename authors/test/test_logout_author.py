from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthorLogoutTest(TestCase):
    def test_user_tries_to_logout_used_get_method(self):
        User.objects.create_user(username='my_user', password='my_password')
        self.client.login(username='my_user', password='my_password')

        response = self.client.get(reverse('authors:logout'), follow=True)

        self.assertIn('Invalid logout request', response.content.decode('utf-8'))

    def test_user_tries_to_logout_another_user(self):
        User.objects.create_user(username="my_user", password="my_pass")
        self.client.login(username="my_user", password="my_pass")

        response = self.client.post(reverse('authors:logout'), data={'username': 'another_user'}, follow=True)

        self.assertIn('Invalid logout user', response.content.decode('utf-8'))

    def test_user_tries_to_logout_my_user(self):
        User.objects.create_user(username="my_user", password="my_pass")
        self.client.login(username="my_user", password="my_pass")

        response = self.client.post(reverse('authors:logout'), data={'username': 'my_user'}, follow=True)

        self.assertIn('logout user successfuly', response.content.decode('utf-8'))