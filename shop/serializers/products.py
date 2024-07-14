from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    sub_category = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'image', 'price', 'category', 'sub_category')
