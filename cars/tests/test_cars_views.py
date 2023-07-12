from django.urls import reverse, resolve
from cars import views
from .test_cars_base import CarsViewTest
from cars.models import Cars


class ResolveURLsTest(CarsViewTest):
    def tearDown(self) -> None:
        return super().tearDown()

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
        Cars.objects.get(pk=1).delete()
        response = self.client.get(reverse('car:home'))
        self.assertIn('NO CARS FOUND', response.content.decode('utf-8'))

    def test_car_home_template_loads_cars(self):
        response = self.client.get(reverse('car:home'))
        content = response.content.decode('utf-8')
        response_context_car = response.context['cars']

        self.assertIn('car Title', content)
        self.assertIn('100', content)
        self.assertEqual(len(response_context_car), 1)

    def test_cars_shop_view_is_valid(self):
        view = resolve(reverse('car:Shop', kwargs={'shop_id': 1}))
        self.assertIs(view.func, views.Shop)

    def test_cars_shop_return_404_error_if_not_correct(self):
        Cars.objects.get(pk=1).delete()
        response = self.client.get(reverse('car:Shop', kwargs={'shop_id': 1}))
        self.assertEqual(404, response.status_code)

    def test_cars_car_details_view_is_valid(self):
        view = resolve(reverse('car:cars', kwargs={'id': 1}))
        self.assertIs(view.func, views.Cars_detail)

    def test_cars_car_detail_return_404_error_if_not_car_found(self):
        Cars.objects.get(pk=1).delete()
        response = self.client.get(reverse('car:cars', kwargs={'id': 1}))
        self.assertEqual(404, response.status_code)
