from django.shortcuts import render

from foods.models import FoodCategoryModel, MenuModel, RestaurantsModel

# Create your views here.


def main_page(request):
    return render(request, "foods/main_page.html")

def restaurants_page(request):
    restaurants = RestaurantsModel.objects.all()
    context = {'restaurants':restaurants}
    return render(request, "foods/restaurants.html", context)

def menu(request, restaurant_pk=None):
    category = FoodCategoryModel.objects.all()
    menu = MenuModel.objects.filter(restaurant=restaurant_pk)
    context = {'menu':menu, 'category':category}
    return render(request, "foods/menu.html", context)