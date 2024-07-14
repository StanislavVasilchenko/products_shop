from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_name')
    slug = models.SlugField(blank=True, null=True, verbose_name='slug')
    image = models.ImageField(upload_to='media/categories/', verbose_name='image', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=255, verbose_name='sub_category_name')
    slug = models.SlugField(blank=True, null=True, verbose_name='slug')
    image = models.ImageField(upload_to='media/sub_categories/', verbose_name='image', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.parent_category}'

    class Meta:
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='product_name')
    slug = models.SlugField(blank=True, null=True, verbose_name='slug')
    image = models.ImageField(upload_to='media/products/', verbose_name='image', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products_sub_category')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.category.name} - {self.sub_category.name}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
