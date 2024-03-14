from django.urls import path

from . import views

app_name = 'car'

urlpatterns = [
    path('', views.CarsHomePage.as_view(), name="home"),
    path('cars/search/', views.CarsSearchList.as_view(), name='search'),
    path('cars/shop/<int:shop_id>/', views.CarsShopList.as_view(), name="Shop"),
    path('cars/<int:id>/', views.Cars_detail, name="cars")
]
