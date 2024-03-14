from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path("register/", views.authors_register, name="register"),
    path("create/", views.authors_create, name="create"),
    path("login/", views.authors_login, name="login"),
    path("validation/", views.authors_login_validation, name="validation"),
    path("logout/", views.authors_logout, name="logout"),
    path("dashboard/", views.authors_dashboard, name="dashboard"),
    path("dashboard/create", views.DashboardCars.as_view(), name="dashboard_create"),
    path("dashboard/<int:id>/edit", views.DashboardCars.as_view(), name="dashboard_edit"),
    path("dashboard/<int:id>/delete", views.DashboardDeleteCars.as_view(), name="dashboard_delete"),
]
