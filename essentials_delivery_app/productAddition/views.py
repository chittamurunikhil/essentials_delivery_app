from django.shortcuts import render

#importing http for response
from django.http import HttpResponse

# Create your views here.



# #function based view

# add productname
def productName(request):
    return HttpResponse("<h1>This is product name view<h1><h2>add your products here<h2>")

# add productid
def productId(request):
    return HttpResponse("This is productid view")

# add producttype
def productType(request):
    return HttpResponse("This is producttype view")


# add productquantity
def productQuantity(request):
    return HttpResponse("This is productquantity view")

# add productquality
def productQuality(request):
    return HttpResponse("This is productquality view")

# add productprice
def productPrice(request):
    return HttpResponse("This is productprice view")

# add productimage
def productImage(request):
    return HttpResponse("This is productimage view")