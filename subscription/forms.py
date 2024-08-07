from django import forms
from .models import Subscriber


class SubscriptionForm(forms.ModelForm):
    """
    Form for subscribing users, ensuring uniqueness of email addresses.
    """
    class Meta:
        model = Subscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('You are already subscribed.')
        return email
