from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    price_reg=models.CharField(max_length=30)
    description=models.TextField()
    qauntity=models.IntegerField()
    image=models.CharField(max_length=150)
    weight=models.IntegerField()
    depth=models.IntegerField()
    width=models.IntegerField()
    height=models.IntegerField()
    price_sale=models.CharField(max_length=30)
    bestseller=models.CharField(max_length=20)
    status=models.CharField(max_length=20,null=True)
    date=models.DateField(null=True)
    productlink=models.CharField(max_length=150,null=True)
    category=models.CharField(max_length=30)

class User(models.Model):
    name=models.CharField(blank=True,max_length=100)
    email= models.CharField(blank=True,max_length=100)
    password=models.CharField(blank=True,max_length=15)
    address=models.CharField(blank=True,max_length=100)
    city=models.CharField(blank=True,max_length=20)
    state=models.CharField(blank=True,max_length=20)
    pincode=models.IntegerField(blank=True)
    # country=models.CharField()
    number=models.IntegerField(blank=True)

class UserPurchase(models.Model):
    email=models.ForeignKey(User, on_delete=models.CASCADE)
    productid=models.CharField(max_length=50)
    date=models.DateField()
    qauntity=models.IntegerField()
    month=models.IntegerField(null=True) 
    
class Coupon(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    datefrom=models.DateField()
    dateto=models.DateField()

# class rating(models.Model):
# class reviews(models.Model):

# class payment(models.Model):
