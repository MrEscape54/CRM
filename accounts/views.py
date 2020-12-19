from accounts.models import Account
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import ParentForm, AccountForm

@login_required
def account_list(request):
    accounts = Account.active.all()

    if request.method == 'POST':
        # Instantiate both Account and Parent forms
        account_form = AccountForm(request.POST)
        parent_form = ParentForm(request.POST)

        # if submit is triggered by Account form
        if request.POST.get("form_type") == 'form_account':
            parent_form = ParentForm()
            if account_form.is_valid():
                new_account = account_form.save(commit=False)
                new_account.slug = slugify(new_account.name)
                new_account.save()
                messages.success(request, ('Account successfully created'))
                return redirect('accounts:index')

        # if submit is triggered by Parent form
        elif request.POST.get("form_type") == 'form_parent':
            account_form = AccountForm(initial={'assigned_to': request.user})    
            if parent_form.is_valid():
                new_parent = parent_form.save(commit=False)
                new_parent.created_by = request.user
                new_parent.slug = slugify(new_parent.name)
                new_parent.save()
                messages.success(request, ('Parent Account successfully created'))
                return redirect('accounts:index')
    else: 
        account_form = AccountForm(initial={'assigned_to': request.user})
        parent_form = ParentForm()

    context = {'accounts': accounts, 
               'active': "accounts", 
               'account_form': account_form, 
               'parent_form': parent_form,
               'modal_title': "New Account"
               }

    return render(request, "accounts/index.html", context)

@login_required
def account_detail(request, account):
    account = get_object_or_404(Account, slug=account)

    if request.method == 'POST':
        # Instantiate both Account and Parent forms
        account_form = AccountForm(request.POST or None, instance = account) 
        parent_form = ParentForm(request.POST or None, instance = account.parent_company)

        # if submit is triggered by Account form
        if request.POST.get("form_type") == 'form_account':
            if account_form.is_valid():
                account_form.save()
                messages.success(request, ('Account successfully updated'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # if submit is triggered by Parent form
        elif request.POST.get("form_type") == 'form_parent': 
            if parent_form.is_valid():
                parent_form.save()
                messages.success(request, ('Parent Account successfully updated'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else: 
        account_form = AccountForm(request.POST or None, instance = account)
        parent_form = ParentForm(request.POST or None, instance = account.parent_company)

    context = {'account': account, 
               'active': "accounts", 
               'account_form': account_form, 
               'parent_form': parent_form,
               'modal_title': "Update Account"
               }

    return render(request, "accounts/account_detail.html", context)