from selenium.webdriver.common.by import By
from tests.functional_tests.base import CarsBaseTesting


class CarsHomePageTest(CarsBaseTesting):
    def test_cars_home_page_without_cars_found(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('NO CARS FOUND', body.text)