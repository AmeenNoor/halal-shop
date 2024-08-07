from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid
from django.db.models import Sum
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def calculate_subtotal(self):
        """
        Calculate subtotal of the order
        """
        order_items = OrderItem.objects.filter(order=self)
        subtotal = Sum(item.product.price *
                       item.quantity for item in order_items)
        return subtotal

    def calculate_total(self):
        """
        Calculate total of the order (subtotal + delivery_fee)
        """
        subtotal = self.calculate_subtotal()
        delivery_fee = subtotal * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        total = subtotal + delivery_fee
        return total

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.order.order_number})"
