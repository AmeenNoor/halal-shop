from django.urls import path
from .views import CheckoutView, CheckoutSuccessView

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('success/<str:order_number>/', CheckoutSuccessView.as_view(), name='checkout_success'),
]
