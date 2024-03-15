from unittest.mock import patch
from django.urls import reverse, resolve
from cars import views
from .test_cars_base import CarsViewTest


class RecipeHomeViewsTest(CarsViewTest):

    def test_cars_home_view_is_valid(self):
        view = resolve(reverse('car:home'))
        self.assertIs(view.func.view_class, views.CarsHomePage)

    def test_cars_home_views_returns_status_code_is_ok(self):
        response = self.client.get(reverse('car:home'))
        self.assertEqual(200, response.status_code)

    def test_cars_home_views_loads_template_is_correct(self):
        response = self.client.get(reverse('car:home'))
        self.assertTemplateUsed(response, 'local/pages/home.html')

    def test_cars_home_template_shows_not_found_if_no_cars(self):
        response = self.client.get(reverse('car:home'))
        self.assertIn('NO CARS FOUND', response.content.decode('utf-8'))

    def test_car_home_template_loads_cars(self):
        self.make_car()
        response = self.client.get(reverse('car:home'))
        content = response.content.decode('utf-8')
        response_context_car = response.context['cars']

        self.assertIn('car Title', content)
        self.assertIn('100', content)
        self.assertEqual(len(response_context_car), 1)

    def test_car_home_template_no_loads_cars(self):
        self.make_car(is_published=False)
        response = self.client.get(reverse('car:home'))
        self.assertIn('NO CARS FOUND', response.content.decode('utf-8'))

    def test_invalid_page_query_uses_page(self):
        self.make_car_in_the_batch(10)

        with patch('cars.views.PER_PAGE', new=3):
            response = self.client.get(reverse('car:home') + '?page=1A')
            self.assertEqual(
                response.context['cars'].number,
                1
            )
