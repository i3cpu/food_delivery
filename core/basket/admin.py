from django.contrib import admin

from basket.models import BasketModel, OrdersModel

# Register your models here.

admin.site.register(BasketModel)
admin.site.register(OrdersModel)
