from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account
from contacts.models import Contact
from core.models import User
from core.utils import OPP_STAGES, OPP_SOURCE, CURRENCY_CODES

class Technology(models.Model):
    name = models.CharField(_("Technology"), max_length=64)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="technology_created_by", on_delete=models.PROTECT)

class Opportunity(models.Model):
    name = models.CharField(pgettext_lazy("Name of Opportunity", "Name"), max_length=64)
    account = models.ForeignKey(Account, related_name="opportunities", on_delete=models.CASCADE, blank=True, null=True,)
    slug = models.SlugField()
    stage = models.CharField(pgettext_lazy("Stage of Opportunity", "Stage"), max_length=64, choices=OPP_STAGES)
    source = models.CharField(pgettext_lazy("Source of Opportunity", "Source"), max_length=64, choices=OPP_SOURCE)
    technology = models.ForeignKey(Technology, on_delete=models.PROTECT)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    amount = models.DecimalField(_("Opportunity Amount"), decimal_places=2, max_digits=12, blank=True, null=True)
    contacts = models.ManyToManyField(Contact, related_name="opportunity_contacts")
    closed_on = models.DateField(blank=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(User, related_name="opportunity_assigned_to")
    created_by = models.ForeignKey(User, related_name="opportunity_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)


    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name

