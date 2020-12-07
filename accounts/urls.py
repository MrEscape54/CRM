from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.AccountListView.as_view(), name="index"),
]