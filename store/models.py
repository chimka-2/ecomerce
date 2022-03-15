from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class customer(models.Model):
    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null= True)
    email=models.CharField(max_length=200, null= True)
    
    def __str__(self):
         return self.name


class product(models.Model):
    name = models.CharField(max_length=100,null=True)
    price=models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    image =models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url = ""
        return url


class order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100,null=True)

    def __str__ (self):
        return str(self.id)


class orderItem(models.Model):
    product= models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(order,on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


class ShippingAddress(models.Model):
    customer = models.ForeignKey(customer,on_delete= models.SET_NULL, null=True)
    order = models.ForeignKey(order,on_delete= models.SET_NULL, null=True)
    address =models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=100,null=False)
    zipcode =models.CharField(max_length=200,null=False)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address












