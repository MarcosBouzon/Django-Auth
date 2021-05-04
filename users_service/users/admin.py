from django.contrib import admin
from .models import UserDetails


# Register your models here.
admin.site.register(UserDetails, list_display=("user", "phone", "address", "zip_code", "country"))
