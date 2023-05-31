from django.shortcuts import render, redirect

from basket.models import BasketModel

# Create your views here.

def basket_page(request):
    basket = BasketModel.objects.filter(user = request.user).first()
    products = basket.product.all()
    pproducts_count = products.count() 
    total_price = 0

    for i in products:
        total_price +=i.price

    context = {
        'products':products, 
        'basket':basket, 
        'pproducts_count':pproducts_count,
        'total_price':total_price
          }
    return render(request, 'basket/basket.html', context)

def add_to_basket(request, product_pk):
    print("-------------------------------------------------",*request.GET)
    print(request.GET.get('id'))
    return redirect('menu_page')
