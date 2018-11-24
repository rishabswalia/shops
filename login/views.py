from django.shortcuts import render
from data.models import User
import requests
from urllib.request import urlopen

# Create your views here.
def login(request):
    dict={}
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=User.objects.get(email=email)
        if email==a.email and password==a.password:
            request.session['logged']="1"
            request.session['email']=email
            dict.update({"message":"logged in succesfully"})
        else:
            dict.update({"message":"Incorect username and password"})
    
    return render(request,'login.html',dict)