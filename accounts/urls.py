from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.account_list, name="index"),
    #path("", views.AccountListView.as_view(), name="index"),

    #path("parent-create/", views.ParentCompanyCreateView.as_view(), name="parent_create"),
    #path("account-create/", views.AccountCreateView.as_view(), name="account_create"),
]