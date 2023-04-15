from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    pincode=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    type=models.CharField(max_length=122)

    def __str__(self):
        return (self.phone+','+self.password)
    
class product(models.Model):
    pname=models.CharField(max_length=122)
    sphone=models.CharField(max_length=122)
    price=models.CharField(max_length=122)
    image=models.ImageField(upload_to='product/')

    def __str__(self):
        return (self.sphone)