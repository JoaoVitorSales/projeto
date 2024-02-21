from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest.mock import patch
import pytest
from tests.functional_tests.cars.base import CarsBaseTesting


@pytest.mark.functional_test
class CarsHomePageTest(CarsBaseTesting):
    def test_cars_home_page_without_cars_found(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')   
        self.assertIn('NO CARS FOUND', body.text)

    def test_cars_search_can_find_correct_car(self):
        cars = self.make_car_in_the_batch()

        title_needed = 'Car title 1'

        cars[0].title = title_needed
        cars[0].save()

        # User open the page

        self.browser.get(self.live_server_url)

        # See a place written "Search for a car"

        search_input = self.browser.find_element(By.XPATH, '//input[@placeholder= "SEARCH FOR A CAR"]')

        # His click in the button and written "Car title 1" for find a car

        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        # The user looks at what his looking for

        self.assertIn(title_needed, self.browser.find_element(By.TAG_NAME, 'body').text)

    @patch('cars.views.PER_PAGE', new=2)
    def test_home_page_pagination(self):
        self.make_car_in_the_batch()

        # User open the page

        self.browser.get(self.live_server_url)

        # User see the current page and click in page 2

        page2 = self.browser.find_element(By.XPATH, '//a[@aria-label = "Go to page 2"]')
        page2.click()

        # User see the result

        self.assertEqual(2, len(self.browser.find_elements(By.CLASS_NAME, 'cars')))

        