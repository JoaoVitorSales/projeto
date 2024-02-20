from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_browser_chrome


class CarsBaseTesting(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_browser_chrome()
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()