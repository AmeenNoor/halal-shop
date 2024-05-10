from django.conf import settings

def cart_total(request):
    cart_items = request.session.get('cart', {})
    subtotal = sum(item['price'] * item.get('quantity', 1) for item in cart_items.values() if isinstance(item, dict))
    
    delivery = subtotal * float(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    total = delivery + subtotal

    for item in cart_items.values():
        item['total_per_quantity'] = item['price'] * item.get('quantity', 1)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery': delivery,
        'total': total,
    }

    return context