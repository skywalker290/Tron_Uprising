from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    pincode=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    type=models.CharField(max_length=122)
