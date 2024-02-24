from django.shortcuts import render, HttpResponse
from products.models import *


def product_details(request , name):
    cat = Category.objects.get(category_name=name)
    products = Product.objects.filter(category= cat)
    
    return render(request  , 'product/product_details.html' , context = {'products' : products})



def get_product(request , slug):
    try:
        product = Product.objects.get(slug = slug)
        return render(request  , 'product/product.html' , context = {'product' : product})

    except Exception as e:
        return HttpResponse(e)

