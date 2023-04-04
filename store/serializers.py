from rest_framework import serializers
from .models import (
    Category,
    ProductType,
    ProductSpecification,
    ProductSpecificationValue,
    Product,
    ProductImage,
)


class ProductImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context["product_id"]
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "regular_price",
            "discount_price",
            "category",
            "product_type",
            "slug",
            "images",
            "is_active",
            "created_at",
            "updated_at",
        ]
