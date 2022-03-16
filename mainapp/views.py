from django.shortcuts import render

from .models import Items


def main(request):
    return render(request, 'main_page.html')


def men(request):
    items = Items.objects.select_related().filter(category_id=1)
    return render(request, 'items.html', {'items': items})


def women(request):
    items = Items.objects.select_related().filter(category_id=2)
    return render(request, 'items.html', {'items': items})


def kids(request):
    items = Items.objects.select_related().filter(category_id=3)
    return render(request, 'items.html', {'items': items})


def accessories(request):
    items = Items.objects.select_related().filter(category_id=4)
    return render(request, 'items.html', {'items': items})


def sneakers(request):
    items = Items.objects.select_related().filter(category_id=5)
    return render(request, 'items.html', {'items': items})


def product(request):
    return render(request, 'product.html')


def registration(request):
    return render(request, 'registration.html')
