from django.shortcuts import render 
from products.models import *
from accounts.models import CartItems
from django.contrib.auth.decorators import login_required

# Create your views here.

   
def index(request):
    # c = CartItems.objects.all().count()
    
    context = {'products' : Category.objects.all(), 'banners': BannerImage.objects.all()}
    
    return render(request , 'home/index.html' , context)