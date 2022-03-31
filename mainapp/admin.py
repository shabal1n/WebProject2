from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'image', 'stock', 'size', 'price')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


# class BasketAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product')


admin.site.register(Items, ItemAdmin)

admin.site.register(Brands, BrandsAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Sizes, SizeAdmin)

admin.site.register(Basket)

admin.site.register(DeliveryCompany)

admin.site.register(Transport, TransportAdmin)