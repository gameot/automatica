from rest_framework import serializers

from .models import Shop, Visit


class ShopInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('shop', 'lat', 'long')
