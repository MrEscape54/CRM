from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("contacts/", views.ContactList.as_view(), name='contact-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)