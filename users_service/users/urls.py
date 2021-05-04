from django.urls import path
from .views import register, user_login

urlpatterns = [
    path("register/", register, name="user_register"),
    path("login/", user_login, name="user_login"),
]