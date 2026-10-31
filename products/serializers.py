from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0"
            )

        return value
    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Product name must contain at least 3 characters"
            )

        return value

    def validate(self, data):
        name = data.get("name")
        price = data.get("price")

        if name == "Free Product" and price > 0:
            raise serializers.ValidationError(
                "Free Product must have price 0"
            )

        return data
