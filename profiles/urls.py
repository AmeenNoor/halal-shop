from django.urls import path
from .views import AccountView, OrderHistoryView

urlpatterns = [
    path('', AccountView.as_view(), name='profile'),
    path('order_history/', OrderHistoryView.as_view(), name='order_history'),
]