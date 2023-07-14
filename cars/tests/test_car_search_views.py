from django.urls import reverse, resolve
from cars import views
from .test_cars_base import CarsViewTest


class ResolveURLsTest(CarsViewTest):
    def tearDown(self) -> None:
        return super().tearDown()

    def test_cars_search_view_is_valid(self):
        response = resolve(reverse('car:search'))
        self.assertIs(response.func, views.search)

    def test_cars_search_loads_template_is_correct(self):
        response = self.client.get(reverse('car:search') + '?q=teste')
        self.assertTemplateUsed(response, 'local/pages/search.html')

    def test_car_search_return_error_404_if_not_correct(self):
        response = self.client.get('car:search')
        self.assertEqual(404, response.status_code)

    def test_car_search_was_charged_on_title_and_escaped(self):
        response = self.client.get(reverse('car:search') + '?q=teste')
        self.assertIn(
            'user search for &quot;teste&quot; |', response.content.decode('utf-8'))  # noqa

    def test_car_search_title_is_correct(self):
        title1 = 'this is Flamengo'
        title2 = 'not Vasco da Gama'

        cars1 = self.make_car(
            slug='one', title=title1, author_data={'username': 'one'}
        )

        cars2 = self.make_car(
            slug='two', title=title2, author_data={'username': 'two'}
        )

        search_url = reverse('car:search')
        response1 = self.client.get(f'{search_url} ?q={title1}')
        response2 = self.client.get(f'{search_url} ?q={title2}')

        self.assertIn(cars1, response1.context['cars'])
        self.assertIn(cars2, response2.context['cars'])
