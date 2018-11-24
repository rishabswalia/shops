from django.shortcuts import render
from data.models import Product,User
from . import views
import requests
from django.http import HttpResponsePermanentRedirect

def templateDisplay(dict):
    a=Product.objects.all()

    for xyz in a:
        img=str(xyz.id)+".jpg"
        dict['latest'].append({"pid":xyz.id,"title":xyz.title,"price_reg":xyz.price_reg,"price_sale":xyz.price_sale,"img":img})
    print(dict)   
    return dict

# Create your views here.
def displayfunc(request):
    dict={}
    dict['latest']=[]
    
    logout=request.GET.get("logout")
    if logout == "0":
        request.session.flush()
        return HttpResponsePermanentRedirect('/')
        

    return render(request,'index.html',templateDisplay(dict))