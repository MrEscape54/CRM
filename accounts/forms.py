from django import forms
from .models import Account, ParentCompany

class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentCompany
        fields = ('name', 'category', 'is_active')

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('name', 'country', 'industry', 'parent_company', 'status', 'address', 'website', 'description', 'is_active', 'contacts', 'assigned_to')

        widgets = {
            'created_by' : forms.HiddenInput(),
        }