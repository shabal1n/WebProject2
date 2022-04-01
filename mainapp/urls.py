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
    path('save_review/<int:id>',views.save_review, name='save_review')
]
