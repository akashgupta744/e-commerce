from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)


admin.site.register(Cart)


@admin.register(CartItems)
class CartItemAdmin(admin.ModelAdmin):
    list_display=['pk','cart','user','product']