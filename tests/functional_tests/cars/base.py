from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_browser_chrome
from cars.tests.test_cars_base import CarsMixing
import time


class CarsBaseTesting(StaticLiveServerTestCase, CarsMixing):
    def setUp(self) -> None:
        self.browser = make_browser_chrome()
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def sleep(self, seconds=6):
        time.sleep(seconds)