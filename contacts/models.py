from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import User
from core import utils
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(_("First name"), max_length=255, help_text='Required')
    last_name = models.CharField(_("Last name"), max_length=255, help_text='Required')
    location = models.CharField(_("Location"), max_length=30, choices=utils.COUNTRIES, help_text='Required')
    slug = models.SlugField()
    email = models.EmailField(unique=True,help_text='Required')
    phone = PhoneNumberField(blank=True, null=True)
    notes = models.TextField(_("Notes"), max_length=240,  null=True, blank=True)
    position = models.CharField(max_length=64, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="contact_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated on"), auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ["created"]