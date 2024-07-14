from django.contrib import admin
from shop.models import Category, SubCategory, Product


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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'price', 'category', 'sub_category')

    class Meta:
        model = Product
        fields = ('name', 'slug', 'image', 'price', 'category', 'sub_category')
