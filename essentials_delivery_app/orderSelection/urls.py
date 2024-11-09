from django.urls import path
from orderSelection.views import *

urlpatterns = [
    
    path('addprod/' , addProduct),
    path('removeprod/' , removeProduct),
    path('deleteprod/' , deleteProduct),
    path('addwishprod/' , addWishlistProduct),
    path('totalcartvalue/' , totalCartValue),


]