
from rest_framework import serializers
from .models import Product, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'p_title', 'p_description', 'p_prize', 'p_image']


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','p_title', 'p_prize', 'p_image']


# Used for GET
class CartReadSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(read_only=True)
    totalprize = serializers.ReadOnlyField(source='totalprice')

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'totalprize']


# Used for POST, PUT
class CartWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'quantity']