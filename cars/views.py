from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Cars
from django.db.models import Q
from utils.pagination import make_pagination


def home(request):
    car = Cars.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, car, 2)

    return render(request, 'local/pages/home.html', context={
        'cars': page_obj,
        'pagination_range': pagination_range
    })


def Shop(request, shop_id):
    car = get_list_or_404(Cars.objects.filter(
        shop__id=shop_id, is_published=True).order_by('-id'))

    page_obj, pagination_range = make_pagination(request, car, 4)

    return render(request, 'local/pages/shop.html', context={
        'cars': page_obj,
        'pagination_range': pagination_range,
        'title': f'{car[0].shop.name} - Shop',
    })


def Cars_detail(request, id):
    carro = get_object_or_404(Cars, pk=id, is_published=True)

    return render(request, 'local/pages/cars-view.html', context={
        'cars': carro,
        'is_detail_page': True,
    })


def search(request):
    url_search = request.GET.get('q', '').strip()

    if not url_search:
        raise Http404()

    cars = Cars.objects.filter(Q(
        Q(title__icontains=url_search) |
        Q(details__icontains=url_search)
    ), is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, cars, 4)

    return render(request, 'local/pages/search.html', {
        'title_search': f'user search for "{url_search}" |',
        'url_search': url_search,
        'pagination_range': pagination_range,
        'cars': page_obj,
        'additional_url_query': f'&q={url_search}'
    })
