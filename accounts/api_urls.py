from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("accounts/", views.AccountList.as_view(), name='account-list'),
    path("parents/", views.ParentAccountList.as_view(), name='parent-account-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

