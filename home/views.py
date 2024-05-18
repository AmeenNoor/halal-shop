from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product


class HomeView(TemplateView):
    """
    View for home page
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.order_by('-id')[:3]
        return context
