from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, ProductImage, ProductOption


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serialization
    """
    class Meta:
        model = Product
        fields = "__all__"
