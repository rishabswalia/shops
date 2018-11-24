from django.shortcuts import render
from urllib.parse import urlparse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from urllib.request import urlopen
import re
import datetime
import json
from django.core.exceptions import ObjectDoesNotExist
from data.models import Product,Coupon,User,UserPurchase
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect


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
    

def saveModel(name,email1,pincode,password,number,city,address,state):
    if name != None:
        try:
            a=User.objects.get(email=email1)
            dict.update({"print":"User exits already try different email"})
            print(dict)
            return False
        except User.DoesNotExist:
            pro1=User(name=name,
            email=email1,
            pincode=pincode,
            password=password,
            number=number,
            city=city,
            address=address,
            state=state
            )   
            pro1.save()
            return True





def displayfunc(request):
    dict={}
    isModelStored=False
    red=False
    dict['cart']=[]
    i=0
    j=0
    order_quan=0
    order_total=0
    # quan1=request.GET.get("quan1")
    # pid=request.GET.get("pid")
    loggedin=request.session.get("logged")
    if loggedin == "1" :
        dict.update({"message":"you are logged in"})
        emailcheck=request.session.get('email')
        a=User.objects.get(email=emailcheck)
        dict.update({"name":a.name,"email1":a.email,"number":a.number,"city":a.city,"pincode":a.pincode,"address":a.address,"state":a.state,"disabled":"disabled","type":"hidden","formaction":"/thankyou/"})
    else:
        dict.update({"type":"password"})
        # if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        email1=request.POST.get("email1")
        number=request.POST.get("number")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")
        state=request.POST.get("state")
        address=request.POST.get("address")  
        # dict.update({"check":"1"})
        isModelStored=saveModel(name,email1,pincode,password,number,city,address,state)
                
    if isModelStored == True:
        request.session['email']=email1
        request.session['logged']="1"
        return HttpResponsePermanentRedirect('/thankyou/')
    elif isModelStored==False:  
        dict.update({"print":"user already exists"})
   
   
    #cart seetings
    a=request.session.get('cart')
    dict.update({"cartx":a})
    if a == None:
        dict.update({"message1":"Your Cart is Empty","type_submit":"hidden"})
    else:
        for rs in a:
            pid=a[i]['pid']
            quan1=a[i]['qty']
            getDataOfProduct(pid,dict,quan1)
            i=i+1

        for rs in a:
            order_total = order_total + dict['cart'][j]['total']
            j=j+1
            order_quan= j

        dict.update({"type_submit":"submit"})    

        dict.update({"order_total":order_total,"order_quan":order_quan})
        
        
    
    
    print(dict)
    # importFromForm(name,password,email,number,city,state,address)
    return render(request,'checkout.html',dict)