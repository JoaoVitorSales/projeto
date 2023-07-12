from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_cars_home_url_is_correct(self):
        homeUrl = reverse('car:home')
        self.assertEqual(homeUrl, '/')

    def test_cars_shop_url_is_correct(self):
        shopUrl = reverse('car:Shop', kwargs={'shop_id': 1})
        self.assertEqual(shopUrl, '/cars/shop/1/')

    def test_cars_car_details_url_is_correct(self):
        cars_detailUrl = reverse('car:cars', kwargs={'id': 1})
        self.assertEqual(cars_detailUrl, '/cars/1/')
