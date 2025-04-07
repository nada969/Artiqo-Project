from rest_framework import serializers
from .models import order_item , OrderArt , Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderArt
        fields = '__all__'


class orderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = order_item
        fields = '__all__'