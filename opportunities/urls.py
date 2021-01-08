from django.urls import path
from . import views

app_name = 'opportunities'

urlpatterns = [
    path("", views.opportunity_list, name="index"),
    path("<slug:opp_slug>", views.opportunity_detail, name="detail"),
    path("won/<slug:opp_slug>", views.won, name="won"), 
    path("lost/<slug:opp_slug>", views.lost, name="lost"), 

]