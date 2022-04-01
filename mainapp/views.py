from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from .models import Items, ProductReview
from .forms import ReviewAdd


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


def product(request,id):
    product = Items.objects.get(id=id)
    related_products=Items.objects.filter(category = product.category).exclude(id=id)[:3]
    reviewForm=ReviewAdd()
    return render(request, 'product.html', {'data':product, 'related_products':related_products, 
    'form':reviewForm}) 

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

# Save Review
def save_review(request,id):
    product=Items.objects.get(pk=id)
    user=request.user
    review=ProductReview.objects.create(
    user=user,
    product=product,
    review_text=request.POST['review_text'],
    review_rating=request.POST['review_rating'],
    )
    return JsonResponse({'bool':True})
    