from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.db.models.deletion import CASCADE



class UserDetails(models.Model):
    """
    Main User model class for working with user database operations.
    This class inherits from the django User class and add own fields.
    """
    user = models.OneToOneField(DjangoUser, on_delete=CASCADE)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    country = models.CharField(max_length=30, null=True)
    
    def __str__(self) -> str:
        return f"{self.phone} {self.address} {self.zip_code} {self.country}"
    
    def __repr__(self) -> str:
        return f"UserDetails(user{self.user.pk}, phone={self.phone}, address={self.address}, zip_code={self.zip_code}, country={self.country})"




