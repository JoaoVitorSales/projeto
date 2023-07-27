from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path("register/", views.authors_register, name="register"),
    path("create/", views.authors_create, name="create")
]
