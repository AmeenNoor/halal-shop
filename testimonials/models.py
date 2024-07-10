from django.db import models


class Testimonial(models.Model):
    """
    Model for customer testimonials.
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
