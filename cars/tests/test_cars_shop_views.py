from django.urls import reverse, resolve
from cars import views
from .test_cars_base import CarsViewTest


class RecipeShopViewsTest(CarsViewTest):

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
        car = self.make_car(is_published=False)
        response = self.client.get(
            reverse('car:Shop', kwargs={'shop_id': car.shop.id}))
        self.assertEqual(404, response.status_code)
