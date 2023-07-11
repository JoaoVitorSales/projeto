from django.urls import path

from . import views

app_name = 'car'

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="home"),
    path('cars/shop/<int:shop_id>/', views.Shop, name="Shop"),
    path('cars/<int:id>/', views.Cars_detail, name="cars"),
]
