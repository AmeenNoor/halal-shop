from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Product
from .forms import ProductForm
from django.contrib import messages


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
        search_query = self.request.GET.get('q')
        queryset = Product.objects.all()

        if category:
            queryset = queryset.filter(category=category)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(
                    category__icontains=search_query)
            )
        # else:
        #     messages.info(self.request, "Please enter a search query.")

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


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(
            self.request, "You do not have permission to access this page.")
        return redirect('products')


class ProductCreate(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    """
    View to create a new product
    """

    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('products')


class ProductUpdate(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    """
    View to update an existing product
    """

    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('products')


class ProductDelete(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    """
    View to delete an existing product
    """

    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products')
