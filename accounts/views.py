from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required 
from django.urls import reverse
# Create your views here.
from accounts.models import *
from products.models import *


def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return redirect('login')


    return render(request ,'accounts/register.html')

@login_required(login_url='login') 
def logout_page(request):
    logout(request)
    return redirect('index')
    

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    

def add_to_cart(request, uid):
    
    variant = request.GET.get('variant')
    
    product = Product.objects.get(uid = uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user = user, is_paid = False)
    cart_item= CartItems.objects.create(cart = cart,user = user, product = product)
    
    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
       
        cart_item.size_variant =  size_variant
        
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

@login_required(login_url='login') 
def cart(request):
    c = CartItems.objects.filter(user=request.user)
    print(c)
    img_list=[]
    for cart in c:
        f = True 
        for im in cart.product.product_image.all():
            if f:
                img_list.append(im)
                f=False
    print(img_list)
    total=0
    i=0
    for p in c :
        total += p.product.price*p.cart_quantity
        p.image=img_list[i].image
        p.save
        i +=1
    
    context = {'carts': c,'total_cart_sum':total,'count':c.count()}
    
    return render(request, 'accounts/cart.html', context)


def cart_add(request,pk):
    obj = CartItems.objects.get(pk=pk)
    obj.cart_quantity += 1
    obj.save()
    return HttpResponseRedirect(reverse('cart' ))

def cart_sub(request,pk):
    obj = CartItems.objects.get(pk=pk)
    if obj.cart_quantity > 1:
        obj.cart_quantity -= 1
        obj.save()
    
    
    return HttpResponseRedirect(reverse('cart' ))   

def cart_remove(request,pk):
    CartItems.objects.get(pk=pk).delete()
    
    return HttpResponseRedirect(reverse('cart' ))   
