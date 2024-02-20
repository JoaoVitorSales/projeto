from selenium.webdriver.common.by import By
import pytest
from tests.functional_tests.cars.base import CarsBaseTesting

@pytest.mark.functional_test
class CarsHomePageTest(CarsBaseTesting):
    def test_cars_home_page_without_cars_found(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('NO CARS FOUND', body.text)