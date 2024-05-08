from django.urls import path
from .views import CartAddView, CartListView

urlpatterns = [
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('', CartListView.as_view(), name='cart'),
]