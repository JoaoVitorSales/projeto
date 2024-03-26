from django.urls import path

from . import views

app_name = 'car'

urlpatterns = [
    path('', views.CarsHomePage.as_view(), name="home"),
    path('cars/search/', views.CarsSearchList.as_view(), name='search'),
    path('cars/shop/<int:shop_id>/', views.CarsShopList.as_view(), name="Shop"),
    path('cars/<int:pk>/', views.CarsDetailList.as_view(), name="cars"),
    path('cars/api/v1/', views.CarsHomePageApi.as_view(), name="home_api_v1"),
    path('cars/api/v1/<int:pk>', views.CarsDetailListApi.as_view(), name="cars_detail_api_v1"),
    path('cars/theory', views.theory, name="theory"),
]
