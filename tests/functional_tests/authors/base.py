from utils.browser import make_browser_chrome
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_browser_chrome()
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def sleep(self, qt=8):
        time.sleep(qt)

    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(By.XPATH, f'//input[@placeholder="{placeholder}"]')