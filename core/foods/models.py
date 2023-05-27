from django.db import models

# Create your models here.

class RestaurantsModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=200)
    adress = models.CharField(max_length=250)
    # image = models.ImageField(upload_to='images', null=True, blank=True, default='default.jpg')
    # category = models.ManyToManyField("FoodCategoryModel", related_name="food_category" )

    def __str__(self) -> str:
        return f'{self.name}'

class FoodCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'

class MenuModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey('RestaurantsModel', on_delete=models.CASCADE, blank=True)
    categories = models.ManyToManyField('FoodCategoryModel', related_name="food_category")
    # image = models.ImageField(upload_to='images', null=True, blank=True, default='default.jpg')


    def __str__(self) -> str:
        return f'{self.name}'
