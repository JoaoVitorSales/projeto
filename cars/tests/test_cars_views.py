from unittest import skip
from django.urls import reverse, resolve
from cars import views
from .test_cars_base import CarsViewTest


class ResolveURLsTest(CarsViewTest):
    def tearDown(self) -> None:
        return super().tearDown()

    # CARS

    def test_cars_home_view_is_valid(self):
        view = resolve(reverse('car:home'))
        self.assertIs(view.func, views.home)

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

    # SHOP

    def test_cars_shop_view_is_valid(self):
        view = resolve(reverse('car:Shop', kwargs={'shop_id': 1}))
        self.assertIs(view.func, views.Shop)

    def test_cars_shop_return_404_error_if_not_correct(self):
        response = self.client.get(reverse('car:Shop', kwargs={'shop_id': 1}))
        self.assertEqual(404, response.status_code)

    def test_car_shop_template_loads_cars_in_filter(self):
        needed_title = 'this is shop page test'
        self.make_car(title=needed_title)
        response = self.client.get(reverse('car:Shop', kwargs={'shop_id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn('this is shop page test', content)

    def test_car_shop_template_no_loads_cars(self):
        recipe = self.make_car(is_published=False)
        response = self.client.get(
            reverse('car:Shop', kwargs={'shop_id': recipe.shop.id}))
        self.assertEqual(404, response.status_code)

    # CARS_DETAIL

    def test_cars_car_details_view_is_valid(self):
        view = resolve(reverse('car:cars', kwargs={'id': 1}))
        self.assertIs(view.func, views.Cars_detail)

    @skip('i see later')
    def test_cars_car_details_return_404_error_if_not_correct(self):
        response = self.client.get(reverse('car:cars', kwargs={'id': 100}))
        self.assertEqual(404, response.status_code)

    def test_cars_car_details_template_loads_one_recipe(self):
        needed_title = 'this is a detail page test'
        self.make_car(title=needed_title)
        response = self.client.get(reverse('car:cars', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn('this is a detail page test', content)

    def test_cars_car_details_template_no_loads_cars(self):
        recipe = self.make_car(is_published=False)
        response = self.client.get(
            reverse('car:Shop', kwargs={'shop_id': recipe.shop.id}))
        self.assertEqual(404, response.status_code)
