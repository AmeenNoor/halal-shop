from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import SubscriptionForm


class SubscribeView(TemplateView):
    """
    View class handling subscription requests, validating form data,
    sending confirmation emails, and displaying appropriate messages.
    """
    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.save()

            context = {'email': subscriber.email}
            email_body = render_to_string(
                'subscription/email/subscription_email.txt',
                context
            )

            send_mail(
                subject='Subscription Confirmation',
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )

            messages.success(
                request,
                'Thank you for subscribing! '
                'A confirmation email has been sent.'
            )
        else:
            email = request.POST.get('email')
            messages.warning(
                request,
                f'You are already subscribed with {email}.'
            )

        return redirect(request.META.get('HTTP_REFERER', '/'))
