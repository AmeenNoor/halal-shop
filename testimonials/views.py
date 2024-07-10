from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm


class TestimonialListView(FormMixin, ListView):
    """
    View to display and submit testimonials.
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/testimonials_list.html'
    context_object_name = 'testimonials'
    queryset = Testimonial.objects.filter(
                            approved=True).order_by('-created_at')
    success_url = reverse_lazy('testimonial_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.approved = False
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
