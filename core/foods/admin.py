from django.contrib import admin
from foods.models import RestaurantsModel, FoodCategoryModel, MenuModel

# Register your models here.


admin.site.register(RestaurantsModel)
admin.site.register(FoodCategoryModel)
admin.site.register(MenuModel)
