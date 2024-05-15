from django.shortcuts import render
from django.views.generic import TemplateView, LoginRequiredMixin
from .models import UserProfile

class AccountView(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'profile.html'
