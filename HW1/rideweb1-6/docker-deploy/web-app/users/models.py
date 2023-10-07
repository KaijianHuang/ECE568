from django.db import models
from django.contrib.auth.models import User

class Rider(User):
    phone = models.BigIntegerField()
    def __str__(self):
        return f'Rider {self.user.username}'

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Brith = models.DateField()
    maxP = models.IntegerField()
    PlateNum = models.CharField(max_length=100)
    LicenseNum = models.CharField(max_length=100)
    Special = models.CharField(max_length=100)
    Color = models.CharField(max_length = 100)
    Vtype = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'Driver {self.user.username}'