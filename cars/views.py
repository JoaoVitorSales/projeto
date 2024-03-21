import os

from django.http import Http404, JsonResponse
from django.http.response import HttpResponse
from django.forms.models import model_to_dict
from cars.models import Cars
from django.views.generic import DetailView, ListView
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
        car = car.select_related('shop', 'author')
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

        if not url_search:
            raise Http404()
        
        car = car.filter(
            Q(title__icontains=url_search) |
            Q(details__icontains=url_search)
        )
        return car
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        url_search = self.request.GET.get('q', '')
        context.update({'title_search': f'Search for "{url_search}" |', 'url_search': url_search, 'additional_url_query': f'&q={url_search}'})
        
        return context
    

class CarsShopList(ListView):
    model = Cars
    context_object_name = 'cars'
    template_name = 'local/pages/shop.html'
    ordering = ['-id']

    def get_queryset(self, *args, **kwargs):
        car = super().get_queryset(*args, **kwargs)
        car = car.filter(shop__id=self.kwargs.get('shop_id'), is_published=True)
        if not car:
            raise Http404()
        return car

 
class CarsDetailList(DetailView):
    model = Cars
    context_object_name = "car"
    template_name = 'local/pages/cars-view.html'

    def get_queryset(self, *args, **kwargs):
        context = super().get_queryset(*args, **kwargs)
        context = context.filter(is_published=True)
        return context
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'is_detail_page': True})
        return context
    

class CarsHomePageApi(CarsHomePage):
    template_name = 'local/pages/home.html'

    def render_to_response(self, context, **response_kwargs):
        cars = self.get_context_data()['cars']
        cars_list = cars.object_list.values()
        
        return JsonResponse(
            list(cars_list),
            safe=False
        )
    

class CarsDetailListApi(CarsDetailList):
    def render_to_response(self, context, **response_kwargs):
        cars = self.get_context_data()['car']
        cars_list = model_to_dict(cars)

        if cars_list.get('cover'):
            cars_list['cover'] = cars_list['cover'].url[1:] 
        else:
            cars_list['cover'] = ""

        del cars_list['is_published']
        return JsonResponse(
            cars_list,
            safe=False
        )