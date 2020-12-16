from django import forms
from django.forms.models import ModelChoiceField
from .models import Account, ParentCompany

class ParentCreateForm(forms.ModelForm):
    class Meta:
        model = ParentCompany
        fields = ('name', 'category')

class AccountCreateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('name', 'country', 'industry', 'parent_company', 'status', 'address', 'website', 'description', 'is_active', 'contacts', 'assigned_to')

        widgets = {
            'created_by' : forms.HiddenInput(),
        }


