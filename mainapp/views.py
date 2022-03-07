from django.shortcuts import render
from .models import Items


def main(request):
    return render(request, 'main_page.html')


def men(request):
    items = Items.objects.filter(category='Men')
    return render(request, 'items.html', {'items': items})


def women(request):
    items = Items.objects.filter(category='Women')
    return render(request, 'items.html', {'items': items})


def kids(request):
    items = Items.objects.filter(category='Kids')
    return render(request, 'items.html', {'items': items})


def accessories(request):
    items = Items.objects.filter(category='Accessories')
    return render(request, 'items.html', {'items': items})


def sneakers(request):
    items = Items.objects.filter(category='Sneakers')
    return render(request, 'items.html', {'items': items})
