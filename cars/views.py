import os

from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from cars.models import Cars
from django.views.generic.list import ListView
from django.db.models import Q
from utils.pagination import make_pagination

PER_PAGE = os.environ.get('PER_PAGE', 6)


class CarsHomePage(ListView):

    model = Cars 
    context_object_name = 'cars'
    ordering = ['-id']
    template_name = 'local/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        car = super().get_queryset(*args, **kwargs)
        car = car.filter(is_published=True)
        return car
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        page_obj, pagination_range = make_pagination(self.request, context.get('cars'), PER_PAGE)
        context.update({"cars": page_obj, 'pagination_range': pagination_range})
        
        return context
    

class CarsSearchList(ListView):
    model = Cars
    context_object_name = 'cars'
    ordering = ['-id']
    template_name = 'local/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        car = super().get_queryset(*args, **kwargs)
        url_search = self.request.GET.get('q', '').strip()
        car = car.filter(
            Q(title__icontains=url_search) |
            Q(details__icontains=url_search)
        )
        return car
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        url_search = self.request.GET.get('q', '')
        context.update({'url_search': url_search, 'additional_url_query': f'&q={url_search}', 'page_title': f'Search for "{url_search}" |'})
        
        return context
    

class CarsShopList(ListView):
    model = Cars
    context_object_name = 'cars'
    template_name = 'local/pages/shop.html'
    ordering = ['-id']

    def get_queryset(self, *args, **kwargs):
        car = super().get_queryset(*args, **kwargs)
        car = car.filter(shop__id=self.kwargs.get('shop_id'))
        return car


def home(request):
    car = Cars.objects.filter(is_published=True)
    page_obj, pagination_range = make_pagination(request, car, PER_PAGE)

    return render(request, 'local/pages/home.html', context={
        'cars': page_obj,
        'pagination_range': pagination_range
    })


def Shop(request, shop_id):
    car = get_list_or_404(Cars.objects.filter(
        shop__id=shop_id, is_published=True).order_by('-id'))

    page_obj, pagination_range = make_pagination(request, car, PER_PAGE)

    return render(request, 'local/pages/shop.html', context={
        'cars': page_obj,
        'pagination_range': pagination_range,
        'title': f'{car[0].shop.name} - Shop',
    })


def Cars_detail(request, id):
    carro = get_object_or_404(Cars, pk=id, is_published=True)

    return render(request, 'local/pages/cars-view.html', context={
        'car': carro,
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
    )

    page_obj, pagination_range = make_pagination(request, cars, PER_PAGE)

    return render(request, 'local/pages/search.html', {
        'title_search': f'user search for "{url_search}" |',
        'url_search': url_search,
        'pagination_range': pagination_range,
        'cars': page_obj,
        'additional_url_query': f'&q={url_search}'
    })
