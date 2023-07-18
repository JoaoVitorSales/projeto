import math


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
