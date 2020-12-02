from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

#Home view (Biwares home page)
class HomeView(TemplateView):
    template_name = "core/home.html"
    authenticated_user_template_name = "core/index.html"

    #If user is legged in redirects to index page
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return [self.authenticated_user_template_name]
        else:
            return [self.template_name]