from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from checkout.models import Order

class AccountView(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'profile.html'

class OrderHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'order_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user=self.request.user)
        context['orders'] = orders
        return context
