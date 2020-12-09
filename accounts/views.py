from accounts.models import Account, ParentCompany
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
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

class ParentCompanyCreateView(LoginRequiredMixin, CreateView):
    model = ParentCompany
    template_name = "accounts/parentCompany_create_form.html"
    login_url = "/"

    fields = ['name', 'category']

    
class AccountCreateView(CreateView):
    model = Account
    template_name = "accounts/account_create_form.html"
