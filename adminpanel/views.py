from django.shortcuts import render
from data.models import Product,User,UserPurchase,Coupon
from django.http import HttpResponse


# Create your views here.

def displayfunc(request):
    pro1=Product(title="Float Recliner",
    price_reg="Rs 750/month",
    description="Rent our Float, a neutral fabric recliner, which merges seamlessly with any decor in your home.",
    qauntity=8,
    image="ridada",
    weight=40,
    depth=90,
    width=80,
    height=110,
    price_sale="Rs 550/month",
    bestseller="yes",
    status="available",
    productlink="/sofa/bcde/",
    category="sofa")

    pro=User(name="Rishab",
    email="rishabwalia@gmail.com",
    password="hello12345",
    number=9971775086,
    pincode=110032,
    city="Delhi",
    address="1/757 West rohtash nagar shahdara",
    state="Delhi")
    

    # Product.objects.all().delete()   
    # for xyz in range(1,20):
    #    Product.objects.filter(id=xyz).delete()
    design=""

    # design ='Printing all Dreamreal entries in the DB : <br>'
    # a = Product.objects.get(title="Dhyanachand Bed (Brown)")
    # design +=a.price_sale + "<br>"
    # list1=["1000","899","899","800","750","750",]
    # i=0
    b=User.objects.get(email="pragya@gmail.com")
    c=b.id

    objects= UserPurchase.objects.filter(email=c)
    for a in objects:
        # xyz.price_reg=list1[i]
        design += a.productid  +"<br>"
        
    # objects = TestModels.objects.all()
    # for xyz in objects:
    #     p=xyz.price
    #     p= str(p)
    #     p = p + "<br>"
    #     design += p
    return HttpResponse(design)