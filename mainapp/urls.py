from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('kids', views.kids, name='kids'),
    path('accessories', views.accessories, name='accessories'),
    path('sneakers', views.sneakers, name='sneakers'),
]
