from django.test import TestCase
from cars.models import Cars, Shop, User


class CarsViewTest(TestCase):
    def setUp(self) -> None:
        shop = Shop.objects.create(name='Ferrari')
        user = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',)
        car = Cars.objects.create(
            shop=shop,
            author=user,
            title='car Title',
            details='car',
            slug='car-slug',
            value_unit='100',
            description='car Description',
            is_published=True,)
        return super().setUp()
