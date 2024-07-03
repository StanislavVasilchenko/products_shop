from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from shop.models import Category, SubCategory
from shop.serializers.sub_categories import SubCategoriesSerializer


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SerializerMethodField()

    def get_sub_categories(self, obj):
        return SubCategoriesSerializer(SubCategory.objects.filter(parent_category=obj), many=True).data

    class Meta:
        model = Category
        fields = ('name', 'image', 'sub_categories')
