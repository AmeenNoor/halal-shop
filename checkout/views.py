import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm
from .models import Order, OrderItem
from products.models import Product
from django.contrib import messages
from cart.contexts import cart_total

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutView(LoginRequiredMixin, CreateView):
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = '/checkout/success/'

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user

        cart_items = self.request.session.get('cart', {})
        subtotal = sum(item['price'] * item.get('quantity', 1)
                       for item in cart_items.values() if isinstance(item, dict))
        delivery = subtotal * \
            float(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        total = subtotal + delivery

        order.subtotal = subtotal
        order.total = total
        order.delivery_fee = delivery
        order.save()

        line_items = []

        for item_id, item in cart_items.items():
            try:
                product = Product.objects.get(pk=item_id)
            except Product.DoesNotExist:
                messages.error(self.request, (
                    "One of the products in your cart wasn't "
                    "found in our database. "
                    "Please call us for assistance!")
                )
                order.delete()
                return redirect(reverse('cart'))

            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity']
            )

            line_item = {
                'price_data': {
                    'currency': settings.STRIPE_CURRENCY,
                    'product_data': {
                        'name': product.name,
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
            success_url=self.request.build_absolute_uri(
                reverse('checkout_success')),
            cancel_url=self.request.build_absolute_uri(
                reverse('checkout_cancel')),
        )

        return redirect(session.url)


class CheckoutSuccessView(View):
    def get(self, request):
        order = Order.objects.filter(user=request.user).latest('date')
        context = {
            'order': order,
            'order_items': order.items.all(), 
            'order_subtotal': order.subtotal,
            'delivery_fee': order.delivery_fee,
        }
        request.session['cart'] = {}
        return render(request, 'success.html', context)


class CheckoutCancelView(View):
    def get(self, request):
        return render(request, 'cancel.html')
