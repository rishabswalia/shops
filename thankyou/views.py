from django.shortcuts import render
from data.models import Product,Coupon,User,UserPurchase
from django.http import HttpResponse
import requests
from datetime import timedelta  
import datetime
from . import views
# Create your views here.
def displayfunc(request):
    dict={}
    i=0
    dict['show']=[]
    email1=request.session.get("email")
    if request.method=="POST":  
        a=request.session.get('cart')
        b=User.objects.get(email=email1)

        for rs in a:
            
            pid=a[i]['pid']
            quan1=a[i]['qty']
            up=UserPurchase(email=b,
            productid=pid,
            date=datetime.date.today(),
            qauntity=quan1)
                    
            up.save()
            
            dict.update({"bought":"order has been placed"})

    cred=User.objects.get(email=email1)
    c=cred.id
    ded=UserPurchase.objects.filter(email=c)
    for obj in ded:
        date1=obj.date
        date1= date1 + timedelta(days=7)
        s=Product.objects.get(id=obj.productid)
        
        dict['show'].append({"title":s.title,"deliver":date1})




   


    return render(request,'thank.html',dict)