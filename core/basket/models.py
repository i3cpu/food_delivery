from django.db import models

from foods.models import MenuModel

# Create your models here.

class BasketModel(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    product = models.ManyToManyField(MenuModel, related_name="products_basket" )

    def __str__(self) -> str:
        return f'{self.user} - basket'