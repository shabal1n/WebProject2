import datetime
import os

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models

CATEGORIES = (
    ("Men", "Men"),
    ("Women", "Women"),
    ("Kids", "Kids"),
    ("Sneakers", "Sneakers"),
    ("Accessories", "Accessories")
)


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='CATEGORY', choices=CATEGORIES, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Subcategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='SUBCATEGORY', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        ordering = ['title']


class Brands(models.Model):
    title = models.CharField(max_length=255, verbose_name='NAME', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['title']


class Sizes(models.Model):
    title = models.CharField(max_length=255, verbose_name='SIZE', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'
        ordering = ['title']


class Items(models.Model):
    name = models.TextField(default='')
    brand = models.ForeignKey(Brands, blank=True, null=True, on_delete=models.CASCADE, verbose_name='BRAND')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='CATEGORY')
    subcategory = models.ForeignKey(Subcategory, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name='SUBCATEGORY')
    price = models.IntegerField(blank=True, null=True, verbose_name='PRICE')
    image = models.ImageField(null=True, blank=True)
    size = models.ManyToManyField(Sizes)
    stock = models.IntegerField(verbose_name='STOCK')
    description = models.TextField(blank=True)
    order = []

    def __str__(self):
        return f"{self.name}, {self.price} KZT"

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def total(self):
        basket_items = BasketItem.objects.filter(cart=self)
        s = 0
        for basket_item in basket_items:
            s = s + basket_item.item.price * basket_item.count

        return s

    def get_id(self):
        return self.user.id

    def __str__(self):
        return f"Cart of {self.user.username}, total: {self.total()} KZT"


class BasketItem(models.Model):
    cart = models.ForeignKey(Basket, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item}, {self.count} pc"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery = models.ForeignKey('DeliveryCompany', on_delete=models.SET_NULL, blank=True, null=True)
    paid = models.BooleanField(default=False)
    basket = models.ForeignKey(Basket, on_delete=models.DO_NOTHING, default='')
    created_at = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)


class DeliveryCompany(models.Model):
    title = models.CharField(max_length=155, verbose_name='Company Name', default='3')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Delivery Company'
        verbose_name_plural = 'Delivery Companies'


# Product Review
RATING = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.IntegerField(choices=RATING)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def get_review_rating(self):
        return self.review_rating


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=155, verbose_name='Name', default='')
    surname = models.CharField(max_length=155, verbose_name='Surname', default='')
    address = models.CharField(max_length=155, verbose_name='Address', default='')
    photo = models.ImageField(blank=True, null=True, default='beach.jpg')

    def __str__(self):
        return self.user.username


