from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile

class AccountView(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'profile.html'
