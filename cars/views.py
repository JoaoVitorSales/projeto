from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'local/pages/home.html', context={
        'name': ' João Vitor'
    })
 
 
def cars(request, id):
    return render(request, 'local/pages/cars-view.html', context={
        'name': ' João Vitor'
    })

