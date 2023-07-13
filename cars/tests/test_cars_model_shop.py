from .test_cars_base import CarsViewTest, Cars
from django.core.exceptions import ValidationError


class CarsModelTest(CarsViewTest):
    def setUp(self) -> None:
        self.shop = self.make_shop(
            name='Ferrari'
        )
        return super().setUp()

    def test_shop_was_represetarion(self):
        self.assertEqual(str(self.shop), self.shop.name)

    def test_car_shop_has_more_than_65_letters(self):
        self.shop.name = 'a' * 65
        with self.assertRaises(ValidationError):
            self.shop.full_clean()
