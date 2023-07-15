from django.db import models

from django.conf import settings

from foods.models import MenuModel, RestaurantsModel


# Create your models here.

class BasketModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(MenuModel, related_name="products_basket" )
    # amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user} - basket'
    

class OrdersModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    product = models.ManyToManyField(MenuModel, related_name="ordered_products" )
    created_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status  = models.CharField(max_length=250)

    payment_method = models.CharField(max_length=250, blank=False)
    adress = models.CharField(max_length=250, blank=False)
    messages = models.TextField(max_length=250, blank=True)


    def __str__(self) -> str:
        return f'{self.user} - order'