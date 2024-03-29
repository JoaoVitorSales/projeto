from django.urls import reverse, resolve
from cars import views
from .test_cars_base import CarsViewTest


class RecipeCarsDetailsViewsTest(CarsViewTest):

    def test_cars_car_details_view_is_valid(self):
        view = resolve(reverse('car:cars', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.CarsDetailList)

    def test_cars_car_details_return_404_error_if_not_correct(self):
        response = self.client.get(reverse('car:cars', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, 404)

    def test_cars_car_details_template_loads_one_recipe(self):
        needed_title = 'this is a detail page test'
        self.make_car(title=needed_title)
        response = self.client.get(reverse('car:cars', kwargs={'pk': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(needed_title, content)

    def test_cars_car_details_template_no_loads_cars_published(self):
        self.make_car(is_published=False)
        response = self.client.get(reverse('car:cars', kwargs={'pk': 1}))
        self.assertEqual(404, response.status_code)
