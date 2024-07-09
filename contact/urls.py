from django.urls import path
from .views import ContactFormView, ThankYouView


urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
    path('thanks/', ThankYouView.as_view(), name='thank_you'),
]
