import math
from django.core.paginator import Paginator


def make_pagination_range(
        page_range,
        qty_link,
        page_current):

    middle_range = math.ceil(qty_link / 2)
    start_page = page_current - middle_range
    stop_page = page_current + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_page) if start_page < 0 else 0

    if start_page < 0:
        start_page = 0
        stop_page += start_range_offset

    if stop_page >= total_pages:
        start_page = start_page - abs(total_pages - stop_page)

    pagination = page_range[start_page:stop_page]
    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_link,
        'current_page': page_current,
        'total_pages': total_pages,
        'start_page': start_page,
        'stop_page': stop_page,
        'first_page_out_of_range': page_current > middle_range,
        'last_page_out_of_range': stop_page < total_pages,
    }


def make_pagination(request, queryset, per_page, qty_link=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        qty_link,
        current_page
    )

    return page_obj, pagination_range
