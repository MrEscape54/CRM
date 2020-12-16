from accounts.models import Account, ParentCompany
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from accounts.forms import ParentCreateForm, AccountCreateForm

@login_required
def account_list(request):
    accounts = Account.active.all()

    if request.method == 'POST':
        # Instantiate both Account and Parent forms
        account_form = AccountCreateForm(request.POST)
        parent_form = ParentCreateForm(request.POST)

        # if submit is triggered by Account form
        if request.POST.get("form_type") == 'form_account':
            parent_form = ParentCreateForm()
            print(account_form)
            if account_form.is_valid():
                new_account = account_form.save(commit=False)
                new_account.created_by = request.user
                new_account.save()
                messages.success(request, ('Account successfully created'))
                return redirect('accounts:index')

        # if submit is triggered by Parent form
        elif request.POST.get("form_type") == 'form_parent':
            account_form = AccountCreateForm()    
            if parent_form.is_valid():
                new_parent = parent_form.save(commit=False)
                new_parent.created_by = request.user
                new_parent.save()
                messages.success(request, ('Parent Account successfully created'))
                return redirect('accounts:index')
    else: 
        account_form = AccountCreateForm()
        parent_form = ParentCreateForm()

    context = {'accounts': accounts, 
               'active': "accounts", 
               'account_form': account_form, 
               'parent_form': parent_form,
               }

    return render(request, "accounts/index.html", context)

# class AccountListView(LoginRequiredMixin, ListView):
#     queryset = Account.active.all()
#     template_name = "accounts/index.html"
#     login_url = "/"

#     context_object_name = 'accounts'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["active"] = 'accounts'
#         context["parent_form"] = ParentCreateForm()
#         context['account_form'] = AccountCreateForm()

#         return context

# class ParentCompanyCreateView(LoginRequiredMixin, CreateView):
#     model = ParentCompany
#     template_name = "accounts/parentCompany-create.html"
#     login_url = "/"
#     success_url = 'accounts:index'

#     form_class = ParentCreateForm

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.created_by = self.request.user
#         self.object.save()
#         return redirect(self.get_success_url())


    
# class AccountCreateView(LoginRequiredMixin, CreateView):
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
