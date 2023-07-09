from rest_framework import serializers
from foods.models import RestaurantsModel
from foods.models import FoodCategoryModel
from foods.models import MenuModel


class RestaurantsModelSerializer(serializers.ModelSerializer):
    class Meta:
       model = RestaurantsModel
       fields = '__all__'



class FoodCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategoryModel
        fields = '__all__'

        

class MenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'

