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

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        category = self.request.GET.get('category')
        queryset = Product.objects.all()

        if category:
            queryset = queryset.filter(category=category)

        if sort_by == 'name_asc':
            queryset = queryset.order_by('name')
        elif sort_by == 'name_desc':
            queryset = queryset.order_by('-name')
        elif sort_by == 'latest':
            queryset = queryset.order_by('-id') 
        elif sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')

        return queryset
    

class ProductDetail(DetailView):
    """
    View to display product details
    """

    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'