from accounts.models import Account
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import ParentForm, AccountForm

@login_required
def account_list(request):
    accounts = Account.active.all()

    if request.method == 'POST':
        # Instantiate both Account and Parent forms
        account_form = AccountForm(request.POST, prefix='account')
        parent_form = ParentForm(request.POST, prefix='parent')

        # if submit is triggered by Account form
        if request.POST.get("form_type") == 'form_account':
            parent_form = ParentForm(prefix='parent')
            if account_form.is_valid():
                new_account = account_form.save(commit=False)
                new_account.slug = slugify(new_account.name)
                new_account.created_by = request.user
                new_account.save()
                # Mandatory to save m2m relationships if commit= False
                account_form.save_m2m()
                messages.success(request, ('Account has been created successfully'))
                return redirect('accounts:index')

        # if submit is triggered by Parent form
        elif request.POST.get("form_type") == 'form_parent':
            account_form = AccountForm(prefix='account')    
            if parent_form.is_valid():
                new_parent = parent_form.save(commit=False)
                new_parent.created_by = request.user
                new_parent.slug = slugify(new_parent.name)
                new_parent.save()
                messages.success(request, ('Parent Account has been created successfully'))
                return redirect('accounts:index')
    else: 
        account_form = AccountForm(initial={'assigned_to': request.user}, prefix='account')
        parent_form = ParentForm(prefix='parent')

    context = {'accounts': accounts, 
               'active': "accounts", 
               'account_form': account_form, 
               'parent_form': parent_form,
               'modal_account_title': "New Account",
               'modal_parent_title': "New Parent Account",
               }

    return render(request, "accounts/index.html", context)


@login_required
def account_detail(request, account_slug):
    account = get_object_or_404(Account, slug=account_slug)

    if request.method == 'POST':
        # Instantiate both Account and Parent forms
        account_form = AccountForm(request.POST or None, instance = account, prefix='account') 
        parent_form = ParentForm(request.POST or None, instance = account.parent_company, prefix='parent')

        # if submit is triggered by Account form
        if request.POST.get("form_type") == 'form_account':
            if account_form.is_valid():
                account_form.save()
                messages.success(request, ('Account has been updated successfully'))
                return redirect(account)

        # if submit is triggered by Parent form
        elif request.POST.get("form_type") == 'form_parent': 
            if parent_form.is_valid():
                parent_form.save()
                messages.success(request, ('Parent Account has been updated successfully'))
                return redirect(account)
    else: 
        account_form = AccountForm(request.POST or None, instance = account, prefix='account')
        parent_form = ParentForm(request.POST or None, instance = account.parent_company, prefix='parent')

    context = {'account': account, 
               'active': "accounts", 
               'account_form': account_form, 
               'parent_form': parent_form,
               'modal_account_title': "Update Account",
               'modal_parent_title': "Update Parent Account",
               }

    return render(request, "accounts/account_detail.html", context)