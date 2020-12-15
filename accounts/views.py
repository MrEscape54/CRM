from accounts.models import Account, ParentCompany
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from accounts.forms import ParentCreateForm, AccountCreateForm


class AccountListView(LoginRequiredMixin, ListView):
    queryset = Account.active.all()
    template_name = "accounts/index.html"
    login_url = "/"

    context_object_name = 'accounts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = 'accounts'
        context["parent_form"] = ParentCreateForm()
        context['account_form'] = AccountCreateForm()


        return context

class ParentCompanyCreateView(LoginRequiredMixin, CreateView):
    model = ParentCompany
    template_name = "accounts/parentCompany-create.html"
    login_url = "/"
    success_url = 'accounts:index'

    form_class = ParentCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


    
class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/account_create.html"
    login_url = "/"
    success_url = 'accounts:index'

    fields = ['created_by', 'name']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return redirect(self.get_success_url())
