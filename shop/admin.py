from django.contrib import admin
from shop.models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']

    class Meta:
        model = Category
        fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'slug', 'image')

    class Meta:
        model = SubCategory
        fields = ('parent_category', 'name',)
