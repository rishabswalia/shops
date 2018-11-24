from django.shortcuts import render

def contact(request):
    dict={}
    return render(request,'contact.html',dict)


# Create your views here.
