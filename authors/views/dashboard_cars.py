from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from cars.models import Cars
from authors.forms.cars_form import AuthorCarsEdit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='authors:login', redirect_field_name='next'), name='dispatch')
class DashboardCars(View):

    def get_cars(self, id=None):
        cars = None
        if id is not None:

            cars = Cars.objects.filter(is_published=False, author=self.request.user, pk=id).first()

            if not cars:
                raise Http404()
        
        return cars
    
    def render_cars(self, form):
        return render(self.request, 'authors/pages/authors_dashboard_edit.html', context={"forms": form})

    def get(self, request, id=None):

        cars = self.get_cars(id)

        form = AuthorCarsEdit(
            data=request.POST or None,
            files=request.FILES or None,
            instance=cars
        )

        return self.render_cars(form)
    
    def post(self, request, id=None):

        cars = self.get_cars(id)

        form = AuthorCarsEdit(data=request.POST or None,
                              files=request.FILES or None,
                              instance=cars)
        
        if form.is_valid():

            cars = form.save(commit=False)
            cars.author = request.user
            cars.preparation_steps_is_html = False
            cars.is_published = False

            cars.save()

            messages.success(request, 'Your car is saved')
            return redirect(reverse('authors:dashboard_edit', args=(cars.id,)))
        
        return self.render_cars(form)
    

@method_decorator(login_required(login_url='authors:login', redirect_field_name='next'), name='dispatch')
class DashboardDeleteCars(DashboardCars):
    def post(self, *args, **kwargs):
        cars = self.get_cars(self.request.POST.get('id'))
        cars.delete()
        messages.success(self.request, 'Deleted successfully.')
        return redirect(reverse('authors:dashboard'))