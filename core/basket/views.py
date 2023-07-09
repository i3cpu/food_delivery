from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from basket.models import BasketModel, OrdersModel
from foods.models import MenuModel

from django.contrib import messages as m

from rest_framework import mixins, generics
from rest_framework import status
from rest_framework.response import Response
from basket.serializers import BasketModelSerializer
from foods.serializers import MenuModelSerializer
# from basket.forms import OrdersForm

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
    # basket.delete()
    return redirect('basket_page')


def order_products(request):
    basket = BasketModel.objects.filter(user=request.user).first()
    products = basket.product.all()
    total_price = 0
    order = OrdersModel.objects.filter(user = request.user).first()
    # print(order, "----------------------------------")
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
    

def orders_page(request):
    orders = OrdersModel.objects.filter(user = request.user).first()
    products = orders.product.all()
    context = {'products':products, 'orders':orders}
    return render(request, 'basket/orders.html', context)


# -------------api страницы корзины ------------------ 

class BasketAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    basket_serializer_class = BasketModelSerializer
    product_serializer_class = MenuModelSerializer
    serializer_class = basket_serializer_class

    def get_object(self):
        basket = BasketModel.objects.filter(user=self.request.user).first()
        return basket
    

    def get(self, request, *args, **kwargs):
        basket = self.get_object()
        products = basket.product.all()
        products_count = products.count()

        total_price = sum(product.price for product in products)

        serializer = self.basket_serializer_class(basket)
        product_serializer = self.product_serializer_class(products, many=True)

        context = {
            'basket': serializer.data,
            'products': product_serializer.data,
            'products_count': products_count,
            'total_price': total_price,
        }

        return Response(context)
    
# -------------api добавление продуктов в корзину ------------------ 
class AddToBasketAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = BasketModelSerializer

    def get(self, request, product_pk):
        product = get_object_or_404(MenuModel, pk=product_pk)
        basket = BasketModel.objects.filter(user=request.user).first()
        quantity = 0

        if basket is None:
            basket = BasketModel.objects.create(user=request.user)
            quantity = 1

        basket.product.add(product)
        quantity += 1

        serializer = self.get_serializer(basket)
        context = {
            'basket':serializer.data,
            'message':"Successfully added!",
        }
        return Response(context)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



# -------------api удаление продуктов из корзины, ------------------ 
class RemoveFromBAsketAPIView(mixins.DestroyModelMixin, generics.GenericAPIView):

    def get_queryset(self):
        basket = BasketModel.objects.filter(user = self.request.user).first()
        return basket

    def get(self, request,  product_pk):
        basket = self.get_queryset()
        product = MenuModel.objects.get(pk=product_pk)
        if basket is not None:
            if product in basket.product.all():
                basket.product.remove(product_pk)
                context = {
                    'message':f'product {product_pk} removed from basket'
                }
            else:
                context = {
                    'message':f'The product is not being added to the basket'
                }
            return Response(context)
        
        context = {
            'message':f'basket not found'
        }
        return Response(status=status.HTTP_404_NOT_FOUND)


class ClearBasketAPIView(generics.GenericAPIView):
    serializer_class = BasketModelSerializer

    def get_queryset(self):
        basket = BasketModel.objects.filter(user = self.request.user).first()
        return basket

    def get(self, request):
        basket = self.get_queryset()
        if basket:
            basket.product.clear()
        
        serializer = self.get_serializer(basket)
        context = {
            'basket': serializer.data,
            'message':"basked is cleared",
        }

        return Response(context)

        