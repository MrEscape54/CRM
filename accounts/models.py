from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from core import utils

from core.models import User
from contacts.models import Contact

class ParentCompany(models.Model):
    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64, unique=True)
    created_by = models.ForeignKey(User, related_name="parent_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

class Account(models.Model):

    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64, unique=True)
    country = models.CharField(_("Country"), max_length=3, choices=utils.COUNTRIES, blank=True, null=True)
    industry = models.CharField(_("Industry Type"), max_length=255, choices=utils.ACC_INDUSTRY, blank=True, null=True)
    category = models.CharField(_("Category"), max_length=10, choices=utils.ACC_CATEGORY, blank=True, null=True)
    parent_company = models.ForeignKey(ParentCompany, related_name="parent_company", on_delete=models.CASCADE)
    slug = models.SlugField()
    status = models.CharField(_("Status"), max_length=10, choices=utils.ACC_STATUS)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    country = models.CharField(max_length=3, choices=utils.COUNTRIES, blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="account_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    contacts = models.ManyToManyField(Contact, related_name="account_contacts")
    assigned_to = models.ForeignKey(User, related_name="account_assigned_user", on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created"]

