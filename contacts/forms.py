from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('slug', 'created_by', 'created', 'updated')
