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


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review_text', 'review_rating')


admin.site.register(Items, ItemAdmin)

admin.site.register(Names, NameAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Sizes, SizeAdmin)

admin.site.register (ProductReview, ProductReviewAdmin)