from django.urls import path

from authors import views

app_name = "authors"

urlpatterns = [
    path("register/", views.authors_register, name="register"),
    path("create/", views.authors_create, name="create"),
    path("login/", views.authors_login, name="login"),
    path("validation/", views.authors_login_validation, name="validation"),
    path("logout/", views.authors_logout, name="logout"),
]
