from django.shortcuts import render
from data.models import Product,User,UserPurchase,Coupon
# Create your views here.
produrl=""#isproductmatched
prodcategory=""#getproductinfo
# def isProductMatched():

    

def getProductInfo(pid,dict):
    a = Product.objects.get(id=pid)
    dict.update({"pid":a.id,
    "title":a.title,
    "price_reg":a.price_reg,
    "description":a.description,
    "qauntity":a.qauntity,
    "image":a.image,
    "weight":a.weight,
    "depth":a.depth,
    "width":a.width,
    "height":a.height,
    "price_sale":a.price_sale,
    "bestseller":a.bestseller,
    "status":a.status,
    "date":a.date,
    "productlink":a.productlink,
    "category":a.category,
    })
    prodcategory=a.category
  
    getRelatedProducts(prodcategory,dict)


    return dict

def getRelatedProducts(prodcategory,dict):
    b=Product.objects.filter(category=prodcategory)
    for xyz in b:
        dict['related'].append({"pid":xyz.id,"title":xyz.title,"price_reg":xyz.price_reg,"price_sale":xyz.price_sale,"image":xyz.image})
   
    return dict

def dataMovedToTemplate(request):
    a=request.session.get('cart')
    if a== None:
        request.session['cart']=[]
    request.session.modified = True
    # SESSION_SAVE_EVERY_REQUEST=True 
    dict={}
    dict['related']=[]

    if request.method=="POST":
        pid=request.POST.get("pid")
        qaun1=request.POST.get("quantity")
        deviceArr={"pid":pid,"qty":qaun1}
        request.session['cart'].append(deviceArr)

    a=request.session.get('cart')
    dict.update({"cart":a})
        
        

    
    pid=request.GET.get("pid")

    return render(request,'product.html',getProductInfo(pid,dict))
