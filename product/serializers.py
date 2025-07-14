from rest_framework import serializers
from .models import Product
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    priceAfterTaxes = serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
        model = Product
        fields = '__all__'

# calculate the price after taxes:
    def calculate_tax(self,product:Product):
        return int(product.price * float(1.1))