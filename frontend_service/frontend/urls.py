from django.urls import path
from .views import register, login

urlpatterns = [
    path("register/", view=register, name="frontend_register"),
    path("login/", view=login, name="frontend_login"),
]