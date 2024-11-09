from django.urls import path
from productAddition.views import *

urlpatterns = [
    

    path('addprodname/' , productName),
    path('addprodid/' , productId),
    path('addprodtype/' , productType),
    path('addprodqnty/' , productQuantity),
    path('addprodqlty/' , productQuality),
    path('addprodprice/' , productPrice),
    path('addprodimg/' , productImage),
]