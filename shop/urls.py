from django.urls import path

from shop.apps import ShopConfig
from shop.views import CategoryListAPIView, ProductListAPIView, ProductCreateAPIView

app_name = ShopConfig.name

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('products/', ProductListAPIView.as_view(), name='products-list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='products-create'),
]
