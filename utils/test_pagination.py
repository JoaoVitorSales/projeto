from django.test import TestCase
from utils.pagination import make_pagination_range


class PaginationRange(TestCase):

    def test_if_range_of_pagination_is_correct(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=1
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_if_range_of_start_page_is_correct(self):
        # Current page = 1 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=1
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 2 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=2
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 3 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=3
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        # Current page = 4 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=4
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_if_range_of_middle_page_are_correct(self):

        # Current page = 5 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=5
        )['pagination']
        self.assertEqual([4, 5, 6, 7], pagination)

        # Current page = 7 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=7
        )['pagination']
        self.assertEqual([6, 7, 8, 9], pagination)

    def test_if_range_of_stop_page_is_correct(self):

        # Current page = 8 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=8
        )['pagination']
        self.assertEqual([7, 8, 9, 10], pagination)

        # Current page = 9 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=9
        )['pagination']
        self.assertEqual([7, 8, 9, 10], pagination)

        # Current page = 10 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=10
        )['pagination']
        self.assertEqual([7, 8, 9, 10], pagination)

        # Current page = 11 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 11)),
            qty_link=4,
            page_current=11
        )['pagination']
        self.assertEqual([7, 8, 9, 10], pagination)
