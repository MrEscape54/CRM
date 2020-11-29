from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymice_models

from core.models import User
from opportunities.models import Opportunity

class Note(models.Model):
    body = tinymice_models.HTMLField(_("Note"))
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated on"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="task_created_by", on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, related_name="task_opportunity", on_delete=models.CASCADE)

    def __str__(self):
        return f'Note created by {self.created_by}'

#TODO: Reminders 
class Activity(models.Model):
    pass