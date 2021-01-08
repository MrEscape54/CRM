from django import forms
from .models import Technology, Opportunity, User

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('name',)

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        exclude = ('slug', 'created_by',)

    def __init__(self, *args, **kwargs):
        super(OpportunityForm, self).__init__(*args, **kwargs)
        users = User.objects.all()
        self.fields['assigned_to'].choices = [(user.pk, user.get_full_name()) for user in users]