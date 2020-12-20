from django import forms
from .models import Account, ParentCompany, User

class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentCompany
        fields = ('name', 'category', 'is_active')

class AccountForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        users = User.objects.all()
        self.fields['assigned_to'].choices = [(user.pk, user.get_full_name()) for user in users]

    class Meta:
        model = Account
        fields = ('name', 'country', 'industry', 'parent_company', 'status', 'address', 'website', 'description', 'is_active', 'contacts', 'assigned_to')

        widgets = {
            'created_by' : forms.HiddenInput(),
        }