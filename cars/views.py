from django.shortcuts import render
from utils.cars.fabric import fabric_car


def home(request):
    return render(request, 'local/pages/home.html', context={
        'cars': [fabric_car() for _ in range(10)],
    })
 
 
def cars(request, id):
    return render(request, 'local/pages/cars-view.html', context={
        'car': fabric_car(),
        'is_detail_page': True,
    })

