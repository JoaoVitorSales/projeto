from selenium.webdriver.common.by import By
from .base import CarsBaseTesting


class CarsHomePageFunctionalTest(CarsBaseTesting):
    def test_cars_home_page_without_not_cars_found(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('NO CARS FOUND', body.text)
