from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)
    image = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.category
