from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('kids', views.kids, name='kids'),
    path('accessories', views.accessories, name='accessories'),
    path('sneakers', views.sneakers, name='sneakers'),
    path('product/<int:id>', views.product, name='product'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('cart', views.cart, name='cart'),
    path('cart/delete/<int:part_id>', views.delete_item_cart, name='delete_view'),
    path('save_review/<int:id>', views.save_review, name='save_review'),
    path('change_count/<int:item_id>/<int:count>', views.change_count, name='change_count'),
    path('order', views.make_order, name='order'),
    path('search/<str:name>', views.search, name='search'),
    path('aboutUs', views.aboutUs, name='aboutUs')
]
