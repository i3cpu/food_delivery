from django.contrib import admin
from django.urls import path, include
from basket import views

urlpatterns = [
    path('', views.basket_page, name="basket_page"),
    path('/product/add/<int:restaurant_pk>/<int:product_pk>', views.add_to_basket, name="add_to_basket"),
    path('/product/remove/<int:product_pk>', views.remove_from_basket, name="remove_from_basket"),
    path('/product/clear', views.clear_basket, name="clear_basket"),
    path('/order/products', views.order_products, name="order_products"),
    path('/orders', views.orders_page, name="orders_page"),

    path('/api', views.BasketAPIView.as_view(), name="basket-api"),
    path('/api/product/add/<int:product_pk>', views.AddToBasketAPIView.as_view(), name="basket-api-add-product"),
    path('/api/product/remove/<int:product_pk>', views.RemoveFromBAsketAPIView.as_view(), name="basket-api-remove-product"),
    path('/api/product/clear', views.ClearBasketAPIView.as_view(), name="basket-api-clear-product")



]
