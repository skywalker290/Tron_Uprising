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
    
class workshop(models.Model):
    wname = models.CharField(max_length=122)
    wid = models.CharField(max_length=122)
    wimage = models.ImageField(upload_to='workshop/')
    wabout = models.CharField(max_length=122)
    wrange=models.CharField(max_length=122, default='',null=True, blank=True)
    wcity = models.CharField(max_length=122)
    wdatetime = models.CharField(max_length=122)

    def __str__(self):
        return self.wname

class workshopbook(models.Model):
    wname = models.CharField(max_length=122)
    wid = models.CharField(max_length=122)
    pid= models.CharField(max_length=122)

    def __str__(self):
        return self.pid
