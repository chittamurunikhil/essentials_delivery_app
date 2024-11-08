from django.shortcuts import render

#importing http for response
from django.http import HttpResponse

# Create your views here.



# #function based view

# add product
def addProduct(request):
    return HttpResponse("This is addproduct view")

# remove product
def removeProduct(request):
    return HttpResponse("This is removeproduct view")

# delete product
def deleteProduct(request):
    return HttpResponse("This is deleteproduct view")


# add to wishlist
def addWishlistProduct(request):
    return HttpResponse("This addwishlistproduct view")

# total cart value calculation
def totalCartValue(request):
    return HttpResponse("This totalcartvalue view")



