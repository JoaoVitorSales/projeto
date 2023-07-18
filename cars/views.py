from django.http import Http404
from django.shortcuts import get_list_or_404, render
from .models import Cars
from django.db.models import Q


def home(request):
    car = Cars.objects.filter(is_published=True).order_by('-id')
    return render(request, 'local/pages/home.html', context={
        'cars': car,
    })


def Shop(request, shop_id):
    car = get_list_or_404(Cars.objects.filter(
        shop__id=shop_id, is_published=True).order_by('-id'))
    return render(request, 'local/pages/shop.html', context={
        'cars': car,
        'title': f'{car[0].shop.name} - Shop',
    })


def Cars_detail(request, id):
    car = Cars.objects.filter(
        pk=id, is_published=True).order_by('-id').first()

    return render(request, 'local/pages/cars_view.html', context={
        'cars': car,
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

    return render(request, 'local/pages/search.html', {
        'title_search': f'user search for "{url_search}" |',
        'url_search': url_search,
        'cars': cars,
    })
