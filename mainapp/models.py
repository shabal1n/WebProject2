from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


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

#Product Review
RATING=(
    (1, '1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)    
class ProductReview(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Items, on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING, max_length=150)       

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews' 
