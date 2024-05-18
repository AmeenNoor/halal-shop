from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView
from products.models import Product
from django.contrib import messages


class CartAddView(CreateView):
    """
    View to add a product to the cart
    """

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


class CartListView(ListView):
    """
    View to display all items in the cart
    """

    def get(self, request):
        cart_items = request.session.get('cart', {})
        return render(request, 'cart/cart.html', {'cart_items': cart_items})


class CartDeleteView(DeleteView):
    """
    View to remove an item from the cart
    """

    def post(self, request):
        product_id = request.POST.get('product_id')
        cart_items = request.session.get('cart', {})
        if product_id in cart_items:
            del cart_items[product_id]
            request.session['cart'] = cart_items
            messages.success(request, "Item removed from cart.")
        return redirect('cart')
