from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from cart.contexts import cart_total
import stripe

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        current_cart = cart_total(request)
        total = current_cart['total']
        stripe_total = int(total * 100) 

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret,
            'cart_items': current_cart['cart_items'],
            'subtotal': current_cart['subtotal'],
            'delivery': current_cart['delivery'],
            'total': current_cart['total'],
        }

        return render(request, 'checkout/checkout.html', context)

    def post(self, request):
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.original_cart = cart
            order.stripe_pid = request.POST.get('client_secret', '').split('_secret')[0]
            order.subtotal = sum(item['price'] * item['quantity'] for item in cart.values())
            order.delivery_fee = order.subtotal * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            order.total = order.subtotal + order.delivery_fee
            order.save()

            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, dict):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data.get('quantity', 1),
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

        current_cart = cart_total(request)
        total = current_cart['total']
        stripe_total = int(total * 100)

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            'order_form': order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret,
            'cart_items': current_cart['cart_items'],
            'subtotal': current_cart['subtotal'],
            'delivery': current_cart['delivery'],
            'total': current_cart['total'],
        }

        return render(request, 'checkout/checkout.html', context)

class CheckoutSuccessView(LoginRequiredMixin, View):
    def get(self, request, order_number):
        """
        Handle successful checkouts
        """
        order = get_object_or_404(Order, order_number=order_number)
        messages.success(request, f'Order successfully processed! \
            A confirmation email will be sent to {order.email}.')

        if 'cart' in request.session:
            del request.session['cart']
        
        
        email_body = render_to_string('checkout/confirmation_emails/confirmation_email_body.txt', {'order': order})
        send_mail(
            subject=f'Order Confirmation - {order.order_number}',
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[order.user.email],
            fail_silently=False,
        )

        context = {
            'order': order,
        }

        return render(request, 'checkout/success.html', context)
