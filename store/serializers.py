from rest_framework import serializers
from .models import (
    Category,
    ProductType,
    ProductSpecification,
    ProductSpecificationValue,
    Product,
    ProductImage,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description"]
