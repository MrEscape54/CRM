from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path("", views.contact_list, name="index"),
    path("<slug:contact_slug>", views.contact_detail, name="index"),

]