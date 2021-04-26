from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("opportunities/", views.OpportunityList.as_view(), name='opp-list'),
    path("technologies/", views.TechnologyList.as_view(), name='tech-list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)