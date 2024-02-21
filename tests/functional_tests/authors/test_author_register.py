import pytest
from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):
    def fill_form_dummy_data(self, form):

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def get_form(self):
        return self.browser.find_element(By.XPATH, '/html/body/main/div[2]/form/div[1]')
    
    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')

        callback(form)
        return form

    def test_empty_first_name_error(self):
        def callback(form):
            first_name_folder = self.get_by_placeholder(form, 'Ex.: John')
            first_name_folder.send_keys(' ')
            first_name_folder.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your first name', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error(self):
        def callback(form):
            last_name_folder = self.get_by_placeholder(form, 'Ex.: Doe')
            last_name_folder.send_keys(' ')
            last_name_folder.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your last name', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_username_error(self):
        def callback(form):
            username_folder = self.get_by_placeholder(form, 'Your username')
            username_folder.send_keys(' ')
            username_folder.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('This field is required.', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_email_error(self):
        def callback(form):
            email_folder = self.get_by_placeholder(form, 'Your e-mail')
            email_folder.send_keys('')
            email_folder.send_keys(Keys.ENTER)
            form = self.get_form()
        self.form_field_test_with_callback(callback)

    def test_empty_password_error(self):
        def callback(form):
            password1_folder = self.get_by_placeholder(form, 'Your password')
            password2_folder = self.get_by_placeholder(form, 'Repeat your password')
            password1_folder.send_keys('P@ssw0rd')
            password2_folder.send_keys('P@ssw0rd_Different')
            password2_folder.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Password and password2 must be equal', form.text)
        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Ex.: John').send_keys('First Name')
        self.get_by_placeholder(form, 'Ex.: Doe').send_keys('Last Name')
        self.get_by_placeholder(form, 'Your username').send_keys('my_username')
        self.get_by_placeholder(form, 'Your e-mail').send_keys('email@valid.com')
        self.get_by_placeholder(form, 'Your password').send_keys('P@ssw0rd1')
        self.get_by_placeholder(form, 'Repeat your password').send_keys('P@ssw0rd1')

        form.submit()
        self.assertIn(
            'your user has been created',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )