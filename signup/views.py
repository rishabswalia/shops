from django.shortcuts import render
from data.models import User


def saveModel(name,email1,pincode,password,number,city,address,state):
    if name != None:
        try:
            a=User.objects.get(email=email1)
            dict.update({print:"User exits already try different email"})
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
    if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        email1=request.POST.get("email1")
        number=request.POST.get("number")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")
        state=request.POST.get("state")
        address=request.POST.get("address")  
        dict.update({"type":"password"})
        request.session['email']=email1
        isModelStored=saveModel(name,email1,pincode,password,number,city,address,state)


    
    
    return render(request,'sign_up.html',dict)
# Create your views here.
