from django.test import TestCase
from cars.models import Cars, Shop, User


class CarsMixing:
    def make_shop(self, name='shop'):
        return Shop.objects.create(name=name)

    def make_user(self, first_name='user',
                  last_name='name',
                  username='username',
                  password='123456',
                  email='username@email.com'):
        return User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email)

    def make_car(self, shop_data=None,
                 author_data=None,
                 title='car Title',
                 details='car',
                 slug='car-slug',
                 value_unit='100',
                 description='car Description',
                 is_published=True):

        if shop_data is None:
            shop_data = {}
        if author_data is None:
            author_data = {}

        return Cars.objects.create(shop=self.make_shop(**shop_data),
                                   author=self.make_user(**author_data),
                                   title=title,
                                   details=details,
                                   slug=slug,
                                   value_unit=value_unit,
                                   description=description,
                                   is_published=is_published)
    
    def make_car_in_the_batch(self, qtd=8):
        cars = []
        for i in range(qtd):
            kwargs = {'title': f'recipe title{i}', 'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            car = self.make_car(**kwargs)
            cars.append(car)
        return cars  


class CarsViewTest(TestCase, CarsMixing):
    def setUp(self) -> None:
        return super().setUp()

    
