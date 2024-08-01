from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    sub_category = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'sub_category',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = [
            instance.image.url,
            instance.image_middle.url,
            instance.image_small.url
        ]
        return representation


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
