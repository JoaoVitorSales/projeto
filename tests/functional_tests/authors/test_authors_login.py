import pytest
from .base import AuthorsBaseTest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.objects.create_user(
            username='my_user', password=string_password
        )

        self.browser.get(self.live_server_url + reverse('authors:login'))
 
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        form.submit()

        self.assertIn(
            'you are logged in',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_user_author_login_validation_is_fuction(self):
        self.browser.get(self.live_server_url + reverse('authors:validation'))
        self.assertIn('Not Found', self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_form_login_invalid(self):
        # User open the page

        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User see the form

        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # User put your credentials and click to send

        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')        
        username_field.send_keys(' ')
        password_field.send_keys(' ')

        # Send the form

        form.submit()

        self.assertIn('invalidation Username or Password', self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_form_login_invalid_credentials(self):
        # User open the page

        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User see the form

        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # User put your credentials and click to send

        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')        
        username_field.send_keys('invalid_username')
        password_field.send_keys('invalid_password')

        # Send the form

        form.submit()

        self.assertIn('invalidation credentials', self.browser.find_element(By.TAG_NAME, 'body').text)