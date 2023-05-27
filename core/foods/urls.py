from django.contrib import admin
from django.urls import path, include
from foods import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('restaurants', views.restaurants_page, name="restaurants_page"),
    path('restaurant/menu/<str:restaurant_pk>', views.menu, name="menu"),

    
]
