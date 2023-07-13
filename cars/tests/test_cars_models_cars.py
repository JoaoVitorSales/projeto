from parameterized import parameterized
from .test_cars_base import CarsViewTest, Cars
from django.core.exceptions import ValidationError


class CarsModelTest(CarsViewTest):
    def setUp(self) -> None:
        self.car = self.make_car()
        return super().setUp()

    def make_models_not_default(self):
        car = Cars(shop=self.make_shop(name='arrascaeta'),
                   author=self.make_user(username='Gabigol'),
                   title='car Title',
                   details='car',
                   slug='car-slug',
                   value_unit='100',
                   description='car Description')
        self.car.full_clean()
        self.car.save()
        return car

    @parameterized.expand([('title', 30), ('details', 100), ('value_unit', 8), ('description', 2000)])  # noqa
    def test_the_cars_title_raises_error_if_title_has_more_than_max_letters(self, fields, max_lenght):  # noqa
        setattr(self.car, fields, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.car.full_clean()

    def test_if_is_published_was_false(self):
        cars = self.make_models_not_default()
        self.assertFalse(cars.is_published)
