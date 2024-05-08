from django.shortcuts import render, redirect
from django.views.generic import CreateView
from products.models import Product
from django.contrib import messages


class CartAddView(CreateView):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        product = Product.objects.get(pk=product_id)
        cart_item = {
            'id': product.id,
            'name': product.name,
            'image_url': product.image.url,
            'price': float(product.price),
            'quantity': quantity,
        }

        cart_items = request.session.get('cart', {})
        if product_id in cart_items:
            cart_items[product_id]['quantity'] += quantity
        else:
            cart_items[product_id] = cart_item

        request.session['cart'] = cart_items

        messages.success(request, f"{product.name} added to cart.")
        return redirect('products')
