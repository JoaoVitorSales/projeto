from django.urls import path

from . import views

app_name = 'car'

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="home"),
    path('cars/<int:id>/', views.cars, name="cars")
]