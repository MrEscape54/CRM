from .models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from .serializers import ContactSerializer

from .forms import ContactForm

@login_required
def contact_list(request):
    contacts = Contact.active.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            new_contact.slug = slugify(new_contact)
            new_contact.created_by = request.user
            new_contact.save()
            messages.success(request, ('Contact has been created successfully'))
            return redirect('contacts:index')
    
    else: 
        contact_form = ContactForm()

    context = {'contacts': contacts, 
               'active': "contacts", 
               'contact_form': contact_form, 
               'modal_contact_title': "New Contact",
               }

    return render(request, "contacts/index.html", context)

@login_required
def contact_detail(request, contact_slug):
    contact = get_object_or_404(Contact, slug=contact_slug)
    contact_accounts_pks = contact.account_contacts.all().values_list('pk', flat=True)
    related_contacts = Contact.active.filter(account_contacts__in=contact_accounts_pks).exclude(pk=contact.pk)
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, instance = contact) 
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, ('Contact has been updated successfully'))
            return redirect(contact)

    else:
        contact_form = ContactForm(instance = contact)

    context = {'contact': contact, 
               'related_contacts': related_contacts,
               'active': "contacts", 
               'contact_form': contact_form, 
               'modal_contact_title': "Update contact",
               }

    return render(request, "contacts/contact_detail.html", context)

#API Views
class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, 
                        slug=slugify(serializer.validated_data['name']))