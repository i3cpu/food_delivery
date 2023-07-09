from django.contrib import admin
from django.urls import path, include
from foods import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('restaurants', views.restaurants_page, name="restaurants_page"),
    path('restaurant/menu/<str:restaurant_pk>', views.menu, name="menu_page"),

    path('api/restaurants', views.RestaurantsAPIView.as_view(), name='restaurants-api'),
    path('api/restaurants/<int:restaurant_pk>/menu', views.MenuAPIView.as_view(), name='menu-api'),
]
