from django.shortcuts import render, redirect

from basket.models import BasketModel, OrdersModel
from foods.models import MenuModel

from django.contrib import messages as m

# from basket.forms import OrdersForm

# Create your views here.

def basket_page(request):
    print("-------------------------------",request.POST)
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
        'total_price':total_price,

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
    order = OrdersModel.objects.filter(user = request.user).first()
    print(order, "----------------------------------")
    if order==None:
    
        if request.method == "GET":
            payment_method = request.GET.get('payment_method')
            adress = request.GET.get('adress') 
            messages = request.GET.get('messages') 
            order = OrdersModel.objects.create(
                user = request.user,
                total_price=total_price,
                payment_method = payment_method,
                adress = adress,
                messages = messages
                
                )
            order.product.add(*products)
            basket.product.clear()
            return redirect("basket_page")
    else:
        error = "У вас есть активные заказы !"
        m.add_message(request, m.WARNING, error)
        return redirect("basket_page")
