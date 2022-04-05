from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Items, Basket, BasketItem


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


def cart(request):
    current_user = request.user
    basket = Basket.objects.get(user=current_user)
    items = BasketItem.objects.filter(cart=basket).all()
    return render(request, 'cart.html', {'items': items})


def delete_item_cart(request, part_id=None):
    object_basket = BasketItem.objects.get(item_id=part_id)
    object_basket.delete()
    return redirect('cart')


def product(request, id):
    if request.method == 'POST':
        user = request.user
        item = Items.objects.get(id=id)
        basket_global = Basket.objects.get(id=user.id)

        if Basket.objects.filter(id=user.id):
            tmp = BasketItem.objects.create(cart=basket_global, item=item, count=1)
            tmp.save()
        else:
            basket = Basket.objects.create(user=User.objects.get(id=user.id))
            basket.save()
            tmp = BasketItem.objects.create(cart=basket, item=item, count=1)
            tmp.save()
        return HttpResponseRedirect(request.path_info)
    else:
        product = Items.objects.get(id=id)
        related_products = Items.objects.filter(category=product.category).exclude(id=id)[:3]
        return render(request, 'product.html', {'data': product, 'related_products': related_products})


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail is already in use')
                return redirect('registration')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
