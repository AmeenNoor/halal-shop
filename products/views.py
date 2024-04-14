from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product


class ProductList(ListView):
    """
    View to display all list of all products
    """

    model = Product
    context_object_name = "products"
    template_name = "product_list.html"
