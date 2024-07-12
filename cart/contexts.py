from decimal import Decimal
from django.conf import settings

def cart_total(request):
    cart = request.session.get('cart', {})
    subtotal = sum(Decimal(item['price']) * item['quantity'] for item in cart.values())
    delivery = subtotal * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / Decimal(100)
    total = subtotal + delivery

    cart_items = []
    for item_id, item_data in cart.items():
        item_data['total_per_quantity'] = item_data['price'] * item_data['quantity']
        cart_items.append({
            'id': item_id,
            'name': item_data['name'],
            'quantity': item_data['quantity'],
            'total_per_quantity': item_data['total_per_quantity'],
        })

    return {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery': delivery,
        'total': total,
    }
