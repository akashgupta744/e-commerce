from django.shortcuts import render 
from products.models import *


# Create your views here.


def index(request):
    context = {'products' : Category.objects.all() , 'banners': BannerImage.objects.all()}
    
    return render(request , 'home/index.html' , context)