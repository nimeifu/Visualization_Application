from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant', views.restaurant_data, name='restaurant'),
    path('index', views.index, name='index'),
    path('karaoke', views.karaoke_data, name='karaoke'),
    path('order', views.orders_data, name='order')
]
