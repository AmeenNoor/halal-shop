from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm
from cart.contexts import cart_total

class CheckoutView(LoginRequiredMixin,FormView):
    form_class = CheckoutForm
    template_name = 'checkout.html'
    success_url = '/checkout/success/' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = self.request.session.get('cart', {})
        context.update(cart_total(self.request))
        return context

    def form_valid(self, form):
        return super().form_valid(form)