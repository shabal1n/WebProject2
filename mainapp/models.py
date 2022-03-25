from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='CATEGORY', blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Names(models.Model):
    title = models.CharField(max_length=255, verbose_name='NAME', blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
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
    name = models.ForeignKey(Names, blank=True, null=True, on_delete=models.CASCADE, verbose_name='BRAND', )
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='CATEGORY')
    price = models.IntegerField(blank=True, null=True, verbose_name='PRICE')
    image = models.ImageField(null=True, blank=True,  )
    size = models.ForeignKey(Sizes, blank=True, null=True, on_delete=models.CASCADE, verbose_name='SIZE')
    stock = models.IntegerField(verbose_name='STOCK')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Basket(models.Model):
    product = models.ManyToManyField(Items, blank=True, related_name='PRODUCTS')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
        ordering = ['order']
