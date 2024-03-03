from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from products.models import *
from accounts.models import *


def product_details(request , name):
    c = CartItems.objects.filter(user=request.user).count()
    cat = Category.objects.get(category_name=name)
    products = Product.objects.filter(category= cat)
    
    
    return render(request  , 'product/product_details.html' , context = {'products' : products,'count':c})



def get_product(request , slug):
    c = CartItems.objects.filter(user=request.user).count()
    try:
        product = Product.objects.get(slug = slug)
        context = {'product' : product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price

        
        single_img = product.product_image.all()[0]
        context['single_img'] = single_img
        context['count'] = c

        
        return render(request  , 'product/product.html' , context )

    except Exception as e:
        return HttpResponse(e)
    
def search_bar(request):
    c = CartItems.objects.filter(user=request.user).count()
    if request.method == 'POST':
        search = request.POST['search']
        items_list = Product.objects.filter(product_name__icontains = search)
        
    return render(request,'product/search_product.html',{'products':items_list,'count':c})





