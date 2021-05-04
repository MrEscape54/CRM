from accounts.models import Account
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import ParentForm, AccountForm

@login_required
def account_list(request):
    accounts = Account.active.all()

    account_form = AccountForm(initial={'assigned_to': request.user}, prefix='account')
    parent_form = ParentForm(prefix='parent')

    if request.method == 'POST':
        messages.success(request, ('Account has been created successfully'))


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

    account_form = AccountForm(instance = account, prefix='account')
    parent_form = ParentForm(instance = account.parent_account, prefix='parent')

    if request.method == 'POST':
        messages.success(request, ('Account has been updated successfully'))

    context = {'account': account, 
               'active': "accounts", 
               'account_form': account_form, 
               'parent_form': parent_form,
               'modal_account_title': "Update Account",
               'modal_parent_title': "Update Parent Account",
               }

    return render(request, "accounts/account_detail.html", context)
    