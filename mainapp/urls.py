from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('kids', views.kids, name='kids'),
    path('accessories', views.accessories, name='accessories'),
    path('sneakers', views.sneakers, name='sneakers'),
   # path('product', views.product_detail, name='product_detail'),
    path('product/<str:slug>/<int:id>/', views.product_detail, name='product_detail'),
    #  url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
