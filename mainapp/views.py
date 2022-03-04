from urllib import request
from django.shortcuts import render
from .models import Items

def main(request):
    
    return render(request, 'main_page.html')

def men(request):
    items = Items.objects.all()
    return render(request, 'man.html', {'items': items})

def women(request):
    items = Items.objects.all()
    return render(request, 'woman_page.html', {'items': items})