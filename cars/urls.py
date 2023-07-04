from django.urls import path
from cars.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('home/', home),
    path('contato/', contato),
    path('sobre/', sobre)
]