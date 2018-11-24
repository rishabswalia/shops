from django.shortcuts import render
from urllib.parse import urlparse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from urllib.request import urlopen
from data.models import Product
import re
import json
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def getDataOfProduct(pid,dict,quan1):
    try:
        b=Product.objects.get(id=pid)     
        price=b.price_sale
        price=int(price)
        quan1=int(quan1)
        total=price*quan1

        dict['cart'].append({"title":b.title,"price_sale":b.price_sale,"quan1":quan1,"price":price,"total":total,"pid":b.id})
        return dict
    except Product.DoesNotExist:
        dict.update({"print":"no product found"})
        return dict 
    
    
def getDataFromURL(request,quan1,pid,dict):
    # urlmain = request.get_full_path()
    # data=urlparse(urlmain)
    # qur=data.query
    
    # if quan1 is None:
    #     quan=
    #     quan1=quan
    # else:
    #     quan=quan1
        
    
    getDataOfProduct(pid,dict,quan1)
    

    return dict

def displayfunc(request):
    dict={}
    dict['cart']=[]
    i=0
    order_total=0
    order_quan=0
    j=0
    # pid=request.GET.get("pid")
    a=request.session.get('cart')
    dict.update({"cartx":a})
    if a == None:
        dict.update({"message1":"Your Cart is Empty"})
    else:
        for rs in a:
            pid=a[i]['pid']
            if request.method=="POST":
                quan1=request.POST.get("quan1")
            else:
                quan1=a[i]['qty']
            getDataFromURL(request,quan1,pid,dict)
            i=i+1

        for rs in a:
            order_total = order_total + dict['cart'][j]['total']
            j=j+1
            order_quan= j

        dict.update({"order_total":order_total,"order_quan":order_quan})
        request.session['order_quan']=order_quan
        request.session['order_total']=order_total

    print(dict)
    # pid=request.GET.get("pid")  
    return render(request,'cart.html',dict)  