from django.shortcuts import render,redirect
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm
from cart.contexts import cart_total
import stripe
from django.conf import settings
from django.urls import reverse
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutView(LoginRequiredMixin, CreateView):
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = '/checkout/success/'

    def post(self, request, *args, **kwargs):
        line_items = []
        cart_items = request.session.get('cart', {})
        for item_id, item in cart_items.items():
            line_item = {
                'price_data': {
                    'currency': settings.STRIPE_CURRENCY,
                    'product_data': {
                        'name': item['name'],
                    },
                    'unit_amount': int(item['price'] * 100), 
                },
                'quantity': item['quantity'],
            }
            line_items.append(line_item)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('checkout_success')),
            cancel_url=request.build_absolute_uri(reverse('checkout_cancel')),
        )

        return redirect(session.url)

class CheckoutSuccessView(View):
    def get(self, request): 
        return render(request, 'success.html')

class CheckoutCancelView(View):
    def get(self, request):
        return render(request, 'cancel.html')


