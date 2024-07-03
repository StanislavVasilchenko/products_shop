from rest_framework import serializers

from shop.models import SubCategory


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('name', 'image',)
