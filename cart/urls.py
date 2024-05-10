from django.urls import path
from .views import CartAddView, CartListView, CartDeleteView

urlpatterns = [
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('', CartListView.as_view(), name='cart'),
    path('delete/', CartDeleteView.as_view(), name='cart_delete'),
]