from django.views.generic import TemplateView
from django.shortcuts import redirect, render

#Home view (Biwares home page or account page if logged in)
def home(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")
    else:
        return  render(request, "core/home.html", {})