from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from core.models import User
from core import utils
from phonenumber_field.modelfields import PhoneNumberField

class ActiveContactManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Contact(models.Model):
    first_name = models.CharField(_("First name"), max_length=255, help_text='Required')
    last_name = models.CharField(_("Last name"), max_length=255, help_text='Required')
    location = models.CharField(_("Location"), max_length=30, choices=utils.COUNTRIES, help_text='Required')
    slug = models.SlugField(unique=True)
    email = models.EmailField(unique=True,help_text='Required')
    phone = PhoneNumberField(blank=True, null=True)
    source = models.CharField(_("Source"), max_length=20, choices=utils.CONTACT_SOURCE, default="Account Contact")
    vendor = models.CharField(_("Vendor"), max_length=50, null=True, blank=True)
    position = models.CharField(max_length=64, blank=True, null=True)
    is_lead = models.BooleanField(_("Lead"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_by = models.ForeignKey(User, related_name="contact_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated on"), auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("contacts:index", args=[self.slug])

    class Meta:
        ordering = ["source"]
    
    objects = models.Manager() # The default manager.
    active = ActiveContactManager() # Our custom manager.