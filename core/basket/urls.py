from django.contrib import admin
from django.urls import path, include
from basket import views

urlpatterns = [
    path('', views.basket_page, name="basket_page"),
    path('basket/add/<int:product_pk>', views.add_to_basket, name="add_to_basket"),

]
