from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from core import utils

from core.models import User
from contacts.models import Contact

class ParentCompany(models.Model):
    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64, unique=True, help_text='Required')
    category = models.CharField(_("Category"), max_length=10, choices=utils.ACC_CATEGORY, help_text='Required',)
    created_by = models.ForeignKey(User, related_name="parent_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return self.name


class Account(models.Model):

    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64, unique=True, help_text='Required')
    country = models.CharField(_("Country"), max_length=30, choices=utils.COUNTRIES, help_text='Required')
    industry = models.CharField(_("Industry Type"), max_length=255, choices=utils.ACC_INDUSTRY, help_text='Required')
    parent_company = models.ForeignKey(ParentCompany, related_name="parent_company", on_delete=models.CASCADE, help_text='Required')
    slug = models.SlugField()
    status = models.CharField(_("Status"), max_length=15, choices=utils.ACC_STATUS, default="Prospect", help_text='Required')
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #TODO:  Agregar una columna con deals que sume el total y agregar un modal para ver lista de deals.
    created_by = models.ForeignKey(User, related_name="account_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    contacts = models.ManyToManyField(Contact, related_name="account_contacts", blank=True)
    assigned_to = models.ForeignKey(User, related_name="account_assigned_user", on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["status"]

