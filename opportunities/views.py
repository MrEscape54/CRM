from .models import Opportunity
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import OpportunityForm, TechnologyForm

@login_required
def opportunity_list(request):
    opportunities = Opportunity.objects.all()

    if request.method == 'POST':
        opportunity_form = OpportunityForm(request.POST, prefix='opp')
        technology_form = TechnologyForm(request.POST, prefix='tech')

        # if submit is triggered by Opp form
        if request.POST.get("form_type") == 'form_opp':
            technology_form = TechnologyForm(prefix='tech')
            if opportunity_form.is_valid():
                new_opp = opportunity_form.save(commit=False)
                new_opp.slug = slugify(new_opp.name)
                new_opp.created_by = request.user
                new_opp.closed_by = request.user
                new_opp.save()
                # Mandatory to save m2m relationships if commit= False
                opportunity_form.save_m2m()
                messages.success(request, ('Opportunity has been created successfully'))
                return redirect('opportunities:index')

        # if submit is triggered by Technology form
        elif request.POST.get("form_type") == 'form_tech':
            opportunity_form = OpportunityForm(prefix='opp')    
            if technology_form.is_valid():
                new_tech = technology_form.save(commit=False)
                new_tech.created_by = request.user
                new_tech.slug = slugify(new_tech.name)
                new_tech.save()
                messages.success(request, ('Technology has been created successfully'))
                return redirect('opportunities:index')
    
    opportunity_form = OpportunityForm(initial={'assigned_to': request.user}, prefix='opp')
    technology_form = TechnologyForm(prefix='tech')

    context = {'opportunities': opportunities, 
               'active': "opportunities", 
               'opportunity_form': opportunity_form, 
               'technology_form': technology_form,
               'modal_opportunity_title': "New Opportunity",
               'modal_technology_title': "New Technology",
               }

    return render(request, "opportunities/index.html", context)


@login_required
def opportunity_detail(request, opp_slug):
    opportinity = get_object_or_404(Opportunity, slug=opp_slug)

    if request.method == 'POST':
        # Instantiate both Opp and Tech forms
        opportunity_form = OpportunityForm(request.POST or None, instance = opportinity, prefix='opp') 
        technology_form = TechnologyForm(request.POST or None, instance = opportinity.technology, prefix='tech')

        # if submit is triggered by Opp form
        if request.POST.get("form_type") == 'form_opp':
            if opportunity_form.is_valid():
                opportunity_form.save()
                messages.success(request, ('Opportunity has been updated successfully'))
                return redirect(opportinity)

        # if submit is triggered by Tech form
        elif request.POST.get("form_type") == 'form_tech': 
            if technology_form.is_valid():
                technology_form.save()
                messages.success(request, ('Technology has been updated successfully'))
                return redirect(opportinity)
    
    opportunity_form = OpportunityForm(request.POST or None, instance = opportinity, prefix='opp')
    technology_form = TechnologyForm(request.POST or None, instance = opportinity.technology, prefix='tech')

    context = {'opportinity': opportinity, 
               'active': "opportunities", 
               'opportunity_form': opportunity_form, 
               'technology_form': technology_form,
               'modal_account_title': "Update Opportunity",
               'modal_parent_title': "Update Technology",
               }

    return render(request, "opportunities/opportunity_detail.html", context)