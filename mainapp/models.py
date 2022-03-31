from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='CATEGORY', blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Brands(models.Model):
    title = models.CharField(max_length=255, verbose_name='brand', blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['title']


class Sizes(models.Model):
    title = models.CharField(max_length=255, verbose_name='SIZE', blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'
        ordering = ['title']


class Items(models.Model):
    name = models.TextField(blank=True, default='')
    brand = models.ForeignKey(Brands, blank=True, null=True, on_delete=models.CASCADE, verbose_name='BRAND')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='CATEGORY')
    price = models.IntegerField(blank=True, null=True, verbose_name='PRICE')
    image = models.ImageField(null=True, blank=True)
    size = models.ForeignKey(Sizes, blank=True, null=True, on_delete=models.CASCADE, verbose_name='SIZE')
    stock = models.IntegerField(verbose_name='STOCK')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Basket(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Items, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=155, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='data_published')
    completed_at = models.DateTimeField()
    done = models.BooleanField(default=False, verbose_name='done_items')
    delivery = models.ForeignKey('DeliveryCompany', on_delete=models.SET_NULL, blank=True, null=True)
    transport = models.ForeignKey('Transport', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
        ordering = ['order']


class Transport(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True, verbose_name='Transport Name')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Transport'
        verbose_name_plural = 'Transports'


class DeliveryCompany(models.Model):
    title = models.CharField(max_length=155, blank=True, null=True, verbose_name='Company Name')
    transport = models.ManyToManyField(Transport)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Delivery Company'
        verbose_name_plural = 'Delivery Companies'
