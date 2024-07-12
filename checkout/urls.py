from django.urls import path
from .views import CheckoutView, CheckoutSuccessView, stripe_webhook

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('success/<str:order_number>/', CheckoutSuccessView.as_view(), name='checkout_success'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
]
