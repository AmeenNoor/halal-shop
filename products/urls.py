from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    ProductCreate,
    ProductUpdate,
)

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdate.as_view(), name='product_update'),
]