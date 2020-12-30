import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymice_models

from core.utils import ACT_TYPES
from core.models import User
from opportunities.models import Opportunity

class Note(models.Model):
    body = tinymice_models.HTMLField(_("Note"))
    opportunity = models.ForeignKey(Opportunity, related_name="task_opportunity", on_delete=models.PROTECT)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated on"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="task_created_by", on_delete=models.PROTECT)

    def __str__(self):
        return self.opportunity

class Activity(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    body = tinymice_models.HTMLField(_("Note"))
    activity_type = models.CharField(_("Type of Activity"), choices=ACT_TYPES, max_length=10)
    opportunity = models.ForeignKey(Opportunity, related_name="activity_opportunity", on_delete=models.PROTECT)
    date = models.DateTimeField(_("Date"), default=datetime.date.today)
    is_done = models.BooleanField(_("Done"), default=False)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated on"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="activity_created_by", on_delete=models.PROTECT)

    def __str__(self):
        return self.title