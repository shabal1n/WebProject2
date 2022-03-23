from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'image', 'stock', 'size', 'price')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'order')


admin.site.register(Items, ItemAdmin)

admin.site.register(Names, NameAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Sizes, SizeAdmin)

admin.site.register(Basket, BasketAdmin)