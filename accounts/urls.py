from django.urls import path
from accounts.views import *


urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('logout/' , logout_page , name="logout" ),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/', cart, name="cart"),
   path('add-to-cart/<uid>/', add_to_cart, name="add_to_cart"),
   path('cart_add/<str:pk>', cart_add, name="cart_add"),
   path('cart_sub/<str:pk>', cart_sub, name="cart_sub"),
   path('cart_remove/<str:pk>', cart_remove, name="cart_remove"),


]
