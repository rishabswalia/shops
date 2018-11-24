from django.shortcuts import render
from data.models import Product

def showall(request):
    dict={}
    dict['bed']=[]
    dict['sofa']=[]
    # dict['table']=[]
    # dict['chair']=[]


    a=Product.objects.filter(category="Bed")
    for rs in a:
        dict['bed'].append({"title":rs.title,"price_sale":rs.price_sale,"price_reg":rs.price_reg,"pid":rs.id})
    b=Product.objects.filter(category="sofa")
    for rs in b:
        dict['sofa'].append({"title":rs.title,"price_sale":rs.price_sale,"price_reg":rs.price_reg,"pid":rs.id})

    # c=Product.objects.get(category="table")
    # d=Product.objects.get(category="chair")



    return render(request,'shopall.html',dict)
# Create your views here.
