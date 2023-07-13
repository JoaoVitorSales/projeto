from django.shortcuts import get_list_or_404, render
from .models import Cars


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
    carro = Cars.objects.filter(
        pk=id, is_published=True).order_by('-id').first()

    return render(request, 'local/pages/cars-view.html', context={
        'car': carro,
        'is_detail_page': True,
    })


def search(request):
    return render(request, 'local/pages/search.html')
