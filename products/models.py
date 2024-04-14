from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Meat & Poultry', 'Meat & Poultry'),
        ('Seafood', 'Seafood'),
        ('Dairy & Eggs', 'Dairy & Eggs'),
        ('Fruits & Vegetables', 'Fruits & Vegetables'),
        ('Grains & Flour', 'Grains & Flour'),
        ('Spices & Seasonings', 'Spices & Seasonings'),
        ('Snacks & Sweets', 'Snacks & Sweets'),
        ('Frozen Foods', 'Frozen Foods'),
        ('Canned & Packaged Foods', 'Canned & Packaged Foods'),
        ('Drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
