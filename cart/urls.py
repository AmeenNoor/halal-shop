from django.urls import path
from .views import CartAddView

urlpatterns = [
    path('add/', CartAddView.as_view(), name='cart_add'),
]