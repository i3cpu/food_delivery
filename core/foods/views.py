from django.shortcuts import render

from foods.models import FoodCategoryModel, MenuModel, RestaurantsModel

from basket.models import BasketModel

# Create your views here.


def main_page(request):
    return render(request, "foods/main_page.html")

def restaurants_page(request):
    restaurants = RestaurantsModel.objects.all()
    context = {'restaurants':restaurants}
    return render(request, "foods/restaurants.html", context)

def menu(request, restaurant_pk=None):
    restaurants = RestaurantsModel.objects.all()
    category = FoodCategoryModel.objects.all()
    basket = BasketModel.objects.filter(user = request.user).first()
    menu = MenuModel.objects.filter(restaurant=restaurant_pk)
    context = {'menu':menu, 'category':category,'restaurants':restaurants, 'basket':basket }
    return render(request, "foods/menu.html", context)