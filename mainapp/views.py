from unicodedata import category
from urllib import request
from django.shortcuts import render
from .models import Items

def main(request):
    
    return render(request, 'main_page.html')

def men(request):
    items = Items.objects.filter(category = 'Men')
    return render(request, 'items.html', {'items': items})

def women(request):
    items = Items.objects.filter(category = 'Women')
    return render(request, 'items.html', {'items': items})