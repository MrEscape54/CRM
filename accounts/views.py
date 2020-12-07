from accounts.models import Account
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class AccountListView(LoginRequiredMixin, ListView):
    model = models.Account
    template_name = "accounts/index.html"
    login_url = "/"

    context_object_name = 'accounts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = 'accounts'

        return context
    
