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
    pid=models.CharField(max_length=122)
    pname=models.CharField(max_length=122)
    sphone=models.CharField(max_length=122)
    price=models.CharField(max_length=122)
    image=models.ImageField(upload_to='product/')

    def __str__(self):
        return (self.pid+","+self.pname)
    
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
    
class order(models.Model):
    orderid=models.CharField(max_length=122)
    buyerid=models.CharField(max_length=122)
    sellerid=models.CharField(max_length=122)
    product_name=models.CharField(max_length=122)
    product_id=models.CharField(max_length=122)
    quantity=models.IntegerField()
    order_date=models.DateField(max_length=122)

    def __str__(self):
        return self.orderid+","+self.product_id
