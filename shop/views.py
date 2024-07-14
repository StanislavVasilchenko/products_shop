from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from shop.models import Category, Product
from shop.serializers.categories import CategorySerializer
from shop.serializers.products import ProductSerializer


class Pagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = Pagination


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
