from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'image', 'stock', 'price')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class BasketItemAdmin(admin.TabularInline):
    model = BasketItem


class BasketAdmin(admin.ModelAdmin):
   inlines = [BasketItemAdmin]


admin.site.register(Items, ItemAdmin)

admin.site.register(Brands, BrandAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Sizes, SizeAdmin)

admin.site.register(Basket, BasketAdmin)

admin.site.register(Order)

admin.site.register(DeliveryCompany)