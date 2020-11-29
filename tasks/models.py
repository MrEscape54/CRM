from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import User
from opportunities.models import Opportunity

class Note(models.Model):
    body = models.TextField('comentario')
    created = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated on"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="task_created_by", on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, related_name="task_opportunity", on_delete=models.CASCADE)

    def __str__(self):
        return f'Note created by {self.created_by}'

