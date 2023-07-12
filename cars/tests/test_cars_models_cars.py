from .test_cars_base import CarsViewTest


class CarsModelTest(CarsViewTest):
    def setUp(self) -> None:
        self.car = self.make_car()
        return super().setUp()

    def test_the_test(self):
        car = self.car
        ...
