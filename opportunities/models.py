import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account
from contacts.models import Contact
from core.models import User
from core.utils import OPP_STAGES, OPP_SOURCE, CURRENCY_CODES, OPP_PRIORITY, OPP_CATEGORY

class Technology(models.Model):
    name = models.CharField(_("Technology"), max_length=64)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="technology_created_by", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    name = models.CharField(pgettext_lazy("Name of Opportunity", "Name"), max_length=64)
    account = models.ForeignKey(Account, related_name="opportunities", on_delete=models.CASCADE)
    slug = models.SlugField()
    stage = models.CharField(pgettext_lazy("Stage of Opportunity", "Stage"), max_length=64, choices=OPP_STAGES)
    source = models.CharField(pgettext_lazy("Source of Opportunity", "Source"), max_length=64, choices=OPP_SOURCE)
    priority = models.CharField(_("Priority"), max_length=10, choices=OPP_PRIORITY)
    technology = models.ForeignKey(Technology, on_delete=models.PROTECT)
    category = models.CharField(_("Category"), max_length=50, choices=OPP_CATEGORY)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    amount = models.DecimalField(_("Expected Amount"), decimal_places=2, max_digits=12, blank=True, null=True)
    EDC = models.DateField(_("Estimated Date of Closing"),blank=True, null=True, default=datetime.date.today)
    contacts = models.ManyToManyField(Contact, related_name="opportunity_contacts")
    closed_on = models.DateField(blank=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, related_name="opportunity_assigned_user", on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, related_name="opportunity_created_by", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)


    class Meta:
        ordering = ["stage", 'priority']
        verbose_name_plural = 'Opportunities'

    def __str__(self):
        return self.name

    def account_contacts(self):
        acc_contacts = self.contacts.filter(source="Account Contact")
        return acc_contacts

    def vendor_contacts(self):
        vendor_contacts = self.contacts.filter(source="Vendor Contact")
        return vendor_contacts

    def get_absolute_url(self):
        return reverse("opportunities:detail", args=[self.slug])
    

