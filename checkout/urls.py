from django.urls import path
from .views import CheckoutView, CheckoutSuccessView, CheckoutCancelView

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('success/', CheckoutSuccessView.as_view(), name='checkout_success'),
    path('cancel/', CheckoutCancelView.as_view(), name='checkout_cancel'),
]
