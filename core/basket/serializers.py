from rest_framework import serializers
from basket.models import BasketModel


class BasketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = ['user', ]
    