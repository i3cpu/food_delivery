from django.shortcuts import render, redirect

from basket.models import BasketModel, OrdersModel
from foods.models import MenuModel

# Create your views here.

def basket_page(request):
    basket = BasketModel.objects.filter(user = request.user).first()
    products = basket.product.all()
    products_count = products.count() 
    total_price = 0

    for i in products:
        total_price +=i.price

    context = {
        'products':products, 
        'basket':basket, 
        'pproducts_count':products_count,
        'total_price':total_price
          }
    return render(request, 'basket/basket.html', context)


#надо написать quantity и починить отображение на корзине правильную количеству продуктов и цену

def add_to_basket(request, restaurant_pk, product_pk):
    product = MenuModel.objects.get(pk=product_pk)
    basket = BasketModel.objects.filter(user = request.user).first()
    quantity=0
    if basket==None:
        basket = BasketModel.objects.create(user=request.user)
        basket.product.add(product)
        quantity = 1
    else:
        basket.product.add(product)
        quantity+=1

    return redirect('menu_page',restaurant_pk=restaurant_pk )

def remove_from_basket(request, product_pk):
    basket = BasketModel.objects.filter(user=request.user).first()
    basket.product.remove(product_pk)
    return redirect('basket_page')

def clear_basket(request):
    basket = BasketModel.objects.filter(user = request.user).first()
    basket.product.clear()
    return redirect('basket_page')


def order_products(request):
    basket = BasketModel.objects.filter(user=request.user).first()
    products = basket.product.all()
    total_price = 0
    order = OrdersModel.objects.create(user = request.user, total_price=total_price )
    order.product.add(*products)

    print("---------------------------------------------------", *products)
    # order.product.add(*products)
    return redirect("main_page")