from django.urls import path
from products.views import *

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product"),
    path('product_details/<str:name>' , product_details , name="product_details"),
  
]
