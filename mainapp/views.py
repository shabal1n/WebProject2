from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import ReviewAdd, ContactForm
from django.db.models import Q
from django.core.mail import send_mail, get_connection
from django.conf import settings

FILTERS = {'subcategory': '', 'brand': '', 'price': 0, 'prev_page': ''}


def main(request):
    return render(request, 'main_page.html')


def get_filtered_items(passed_category_id, request):
    items = Items.objects.select_related().filter(category_id=passed_category_id)
    if FILTERS.get('prev_page') != request.path_info:
        FILTERS['subcategory'] = ''
        FILTERS['brand'] = ''
        FILTERS['price'] = 0
        FILTERS['prev_page'] = request.path_info
    if FILTERS['subcategory']:
        list_of_subcategories = []
        sub = Subcategory.objects.all()
        for i in sub:
            if i.title in FILTERS['subcategory']:
                list_of_subcategories.append(i)
        items = items.filter(subcategory__in=list_of_subcategories)
    if FILTERS['brand']:
        list_of_brands = []
        br = Brands.objects.all()
        for i in br:
            if i.title in FILTERS['brand']:
                list_of_brands.append(i)
        items = items.filter(brand__in=list_of_brands)
    if int(FILTERS['price']) > 0:
        items = items.filter(price__lt=FILTERS['price'])
    return items


def men(request):
    items = get_filtered_items(1, request)
    brands = Brands.objects.all()
    subcategories = Subcategory.objects.all()
    if Items.order:
        items = items.order_by(*Items.order)
    return render(request, 'items.html', {'items': items, 'brands': brands, 'subcategories': subcategories})


def women(request):
    items = get_filtered_items(2, request)
    brands = Brands.objects.all()
    subcategories = Subcategory.objects.all()
    if Items.order:
        items = items.order_by(*Items.order)
    return render(request, 'items.html', {'items': items, 'brands': brands, 'subcategories': subcategories})


def kids(request):
    items = get_filtered_items(3, request)
    brands = Brands.objects.all()
    subcategories = Subcategory.objects.all()
    if Items.order:
        items = items.order_by(*Items.order)
    return render(request, 'items.html', {'items': items, 'brands': brands, 'subcategories': subcategories})


def accessories(request):
    items = get_filtered_items(4, request)
    brands = Brands.objects.all()
    subcategories = Subcategory.objects.all()
    if Items.order:
        items = items.order_by(*Items.order)
    return render(request, 'items.html', {'items': items, 'brands': brands, 'subcategories': subcategories})


def sneakers(request):
    items = get_filtered_items(5, request)
    brands = Brands.objects.all()
    subcategories = Subcategory.objects.all()
    if Items.order:
        items = items.order_by(*Items.order)
    return render(request, 'items.html', {'items': items, 'brands': brands, 'subcategories': subcategories})


def product(request, id):
    if request.method == 'POST':
        user = request.user
        item = Items.objects.get(id=id)

        if Basket.objects.filter(user=user):
            basket_global = Basket.objects.get(user=user.id)
            list_items = []

            for i in BasketItem.objects.all():
                if i.cart == basket_global:
                    list_items.append(i.item.id)

            if item.id not in list_items:
                tmp = BasketItem.objects.create(cart=basket_global, item=item, count=1)
                tmp.save()
            else:
                item = BasketItem.objects.get(cart=basket_global, item_id=item.id)
                item.count += 1
                item.save()
        else:
            basket = Basket.objects.create(user=User.objects.get(id=user.id))
            basket.save()
            tmp = BasketItem.objects.create(cart=basket, item=item, count=1)
            tmp.save()
        return HttpResponseRedirect(request.path_info)
    else:
        product = Items.objects.get(id=id)
        reviews = ProductReview.objects.filter(product=product)
        if reviews.__len__() > 0:
            reviews = reviews[0]
        related_products = Items.objects.filter(category=product.category).exclude(id=id)[:3]
        reviewForm = ReviewAdd()
        return render(request, 'product.html',
                      {'data': product, 'review': reviews, 'related_products': related_products, 'form': reviewForm})


def cart(request):
    current_user = request.user
    if Basket.objects.filter(user=current_user.id).exists():
        basket = Basket.objects.get(user=current_user)
    else:
        basket = Basket.objects.create(user=current_user)
        basket.save()
    items = BasketItem.objects.filter(cart=basket).all()
    total = basket.total()
    return render(request, 'cart.html', {'items': items, 'total': total})


def delete_item_cart(request, part_id=None):
    object_basket = BasketItem.objects.filter(item_id=part_id)
    for item in object_basket:
        item.delete()
    return redirect('cart')


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        checkbox = request.POST.get('item_check', False)
        if not username or not email or not password1 or not password2:
            messages.info(request, 'Please, fll in all the fields')
            return redirect('registration')
        else:
            if checkbox:
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
                messages.info(request, 'Please, accept our terms')
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
            return render(request, 'main_page.html')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# Save Review
def save_review(request, id):
    product = Items.objects.get(pk=id)
    user = request.user
    review = ProductReview.objects.create(
        user=user,
        product=product,
        review_text=request.POST['review_text'],
        review_rating=request.POST['review_rating'],
    )
    review.save()
    return JsonResponse({'bool': True})


def change_count(request, item_id, count):
    cart_current = Basket.objects.get(user=request.user)
    item_current = Items.objects.get(pk=item_id)
    basket_item = BasketItem.objects.get(cart=cart_current, item=item_current)
    basket_item.count = count
    basket_item.save()
    return redirect('cart')


def make_order(request):
    cart_current = Basket.objects.get(user=request.user)
    if request.method == 'POST':
        delivery = request.POST['delivery']
        city = request.POST['city']
        address = request.POST['address']
        curr_order = Order.objects.get(user=request.user, basket=cart_current)
        curr_order.city = city
        curr_order.address = address
        curr_order.delivery = DeliveryCompany.objects.get(title=delivery)
        curr_order.save()
        for b_item in BasketItem.objects.filter(cart=Basket.objects.get(user=request.user)).all():
            b_item.delete()
        return redirect('cart')
    else:
        if not Order.objects.filter(user=request.user, basket=cart_current).exists():
            order_this = Order.objects.create(user=request.user, basket=cart_current)
            order_this.save()
        items = BasketItem.objects.filter(cart=cart_current).all()
        total = cart_current.total()
        deliveries = DeliveryCompany.objects.all()
        return render(request, 'order.html', {'items': items, 'total': total, 'deliveries': deliveries})


def search(request, name):
    items = Items.objects.filter(Q(name__icontains=name) | Q(brand__title__icontains=name)).all()
    return render(request, 'search.html', {'items': items})


def aboutUs(request):
    return render(request, 'aboutUs.html')


def change_sort(request, sort):
    Items.order = [sort]
    return redirect(request.META.get('HTTP_REFERER'))


def add_filter(request, filter_name, option):
    FILTERS[filter_name] = option
    return redirect(FILTERS['prev_page'][1:])


def aboutUs(request):
    return render(request, 'aboutUs.html')


def newsPage(request):
    return render(request, 'newsPost.html')


def newsPage2(request):
    return render(request, 'newsPost2.html')


def newsPage3(request):
    return render(request, 'newsPost3.html')


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                settings.EMAIL_HOST_USER,
                ['lil-aisana@mail.ru'],
                cd.get('email', 'noreply@example.com'),
                ['lil-aisana@mail.ru'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contactUs.html', {'form': form, 'item': Items.objects.all(), 'submitted': submitted})


def user_profile(request):
    curr_user = request.user
    if not Customer.objects.filter(user_id=curr_user.id).exists():
        Customer.objects.create(user=request.user).save()
    user = Customer.objects.get(user_id=curr_user.id)
    return render(request, 'user_profile.html', {'user': user})


def address(request):
    curr_user = request.user
    if not Customer.objects.filter(user_id=curr_user.id).exists():
        Customer.objects.create(user=request.user).save()
    user = Customer.objects.get(user_id=curr_user.id)

    if request.method == 'POST':
        address = request.POST['address']
        user.address = address
        user.save()
    return render(request, 'address.html', {'user': user})


def orders(request):
    user = request.user
    orders_of_user = Order.objects.filter(user_id=user.id)
    return render(request, 'orders.html', {'orders': orders_of_user, 'user': user})


def payment(request):
    return render(request, 'payment.html')