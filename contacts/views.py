from .models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ContactForm

@login_required
def contact_list(request, contact_slug=None):
    contacts = Contact.active.all()
    contact = None
    if contact_slug:
        contact = get_object_or_404(Contact, slug=contact_slug)

    if request.method == 'POST':
        if not contact:
                contact_form = ContactForm(request.POST)
                if contact_form.is_valid():
                    new_contact = contact_form.save(commit=False)
                    new_contact.slug = slugify(new_contact)
                    new_contact.created_by = request.user
                    new_contact.save()
                    messages.success(request, ('Contact successfully created'))
                    return redirect('contacts:index')
        else:
            contact_form = ContactForm(request.POST or None, instance=contact)
            if contact_form.is_valid():
                new_contact = contact_form.save(commit=False)
                new_contact.slug = slugify(new_contact)
                new_contact.created_by = request.user
                new_contact.save()
                messages.success(request, ('Contact successfully updated'))
                return redirect('contacts:index')
    else: 
        if contact:
            contact_form = ContactForm(request.POST or None, instance = contact)
        else:
            contact_form = ContactForm()

    context = {'contacts': contacts, 
                'contact': contact,
               'active': "contacts", 
               'contact_form': contact_form, 
               'modal_contact_title': "New Contact",
               }

    return render(request, "contacts/index.html", context)