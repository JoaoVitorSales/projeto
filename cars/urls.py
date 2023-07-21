from django.urls import path

from . import views

app_name = 'car'

urlpatterns = [
    path('', views.home, name="home"),
    path('cars/search/', views.search, name='search'),
    path('cars/shop/<int:shop_id>/', views.Shop, name="Shop"),
    path('cars/<int:id>/', views.Cars_detail, name="cars")
]
