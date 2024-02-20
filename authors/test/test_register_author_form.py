from django.urls import reverse
from parameterized import parameterized
from unittest import TestCase, skip
from authors.forms import RegisterForm
from django.test import TestCase as DjangoTestCase


class TestRegisterAuto(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('password', 'Your password'),
        ('password2', 'Repeat your password')
    ]
    )
    def test_placeholder_of_field_are_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, current_placeholder)

    @parameterized.expand([
        ('password2', 'Password confirm')
    ]
    )
    def test_label_of_fields_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.label
        self.assertEqual(placeholder, current_placeholder)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {'username': 'user',
                          'email': 'email@edasa.com',
                          'first_name': 'wesler',
                          'last_name': 'cabrito',
                          'password': '1fdgg',
                          'password2': '1fdgg'}
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'This field is required.'),
        ('password', 'Password must not be empty'),
        ('password2', 'Please, repeat your password'),
        ('email', 'E-mail is required'),
        ('first_name', 'Write your first name'),
        ('last_name', 'Write your last name')

    ]
    )
    def test_field_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn(msg, response.content.decode())
        self.assertIn(msg, response.context['forms'].errors.get(field))

    def test_filed_username_are_more_than_150_letters(self):
        self.form_data['username'] = 'a' * 151
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = ('Username must have less than 150 characters')

        self.assertIn(msg, response.context['forms'].errors.get('username'))

    def test_filed_username_are_less_than_4_letters(self):
        self.form_data['username'] = 's'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = ('Username must have at least 4 characters')

        self.assertIn(msg, response.context['forms'].errors.get('username'))

    def test_upper_case__letters_lower_case_letters_and_numbers(self):
        self.form_data['password'] = 'abc123'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = (
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        )

        self.assertIn(msg, response.context['forms'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = 'Abc123@235'
        self.form_data['password2'] = 'Abc123@234'

        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = (
            'Password and password2 must be equal'
        )

        self.assertIn(msg, response.context['forms'].errors.get('password'))

    def test_register_get_is_equal_404_error(self):
        url = reverse('authors:create')
        response = self.client.get(url, data=self.form_data, follow=True)
        self.assertEqual(404, response.status_code)

    @skip
    def test_email_is_unique(self):
        url = reverse('authors:create')

        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'User e-mail is already in use'
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_author_created_can_login(self):
        url = reverse('authors:create')

        self.form_data.update({
            'username': 'testuser',
            'password': '@Bc123456',
            'password2': '@Bc123456',
        })

        self.client.post(url, data=self.form_data, follow=True)

        is_authenticated = self.client.login(
            username='testuser',
            password='@Bc123456'
        )

        self.assertTrue(is_authenticated)
