from django.shortcuts import render

from foods.models import FoodCategoryModel, MenuModel, RestaurantsModel
from basket.models import BasketModel


from rest_framework import generics, mixins
from foods.serializers import RestaurantsModelSerializer, FoodCategoryModelSerializer,MenuModelSerializer
# from basket.serializers import BasketModelSerializer


def main_page(request):
    return render(request, "foods/main_page.html")

def restaurants_page(request):
    restaurants = RestaurantsModel.objects.all()
    context = {'restaurants':restaurants}
    return render(request, "foods/restaurants.html", context)

def menu(request, restaurant_pk=None):
    # restaurants = RestaurantsModel.objects.all()
    category = FoodCategoryModel.objects.all()
    basket = BasketModel.objects.filter(user = request.user).first()
    menu = MenuModel.objects.filter(restaurant=restaurant_pk)
    context = {'menu':menu, 'category':category, 'basket':basket }
    return render(request, "foods/menu.html", context)


# -------------api ресторанов ------------------ 
class RestaurantsAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = RestaurantsModel.objects.all()
    serializer_class = RestaurantsModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
# ------------- api меню ------------------ 
class MenuAPIView(generics.ListAPIView):
    serializer_class = MenuModelSerializer

    def get_queryset(self):
        restaurant_pk = self.kwargs.get('restaurant_pk')
        return MenuModel.objects.filter(restaurant = restaurant_pk)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['category'] = FoodCategoryModel.objects.all()
        # context['basket'] = BasketModel.objects.filter(user = self.request.user).first()
        return context
        