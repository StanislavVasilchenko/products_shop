from django.urls import path

from shop.apps import ShopConfig
from shop.views import CategoryListAPIView

app_name = ShopConfig.name

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list')
]
