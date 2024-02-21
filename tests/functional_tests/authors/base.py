from utils.browser import make_browser_chrome
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