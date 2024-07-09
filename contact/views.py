from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Contact
from .forms import ContactForm


class ContactFormView(CreateView):
    """
    View to handle contact form submissions,
    save them to the database, and send a confirmation email.
    """
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        form.save()

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        context = {
            'name': name,
            'email': email,
            'message': message,
        }
        email_body = render_to_string(
                        'contact/email/contact_email.txt', context)

        send_mail(
            subject='Enquiry Received',
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        return super().form_valid(form)


class ThankYouView(TemplateView):
    """
    View to display a thank you message after
    the contact form is submitted.
    """
    template_name = 'contact/thank_you.html'
