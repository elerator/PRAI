from django.shortcuts import render
from django.views.generic import CreateView
from django import forms
from django.forms import ModelForm, Textarea

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.functions import Lower

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.layout import Div

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.core import serializers

from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView

from .forms import *
from .models import ResearchProject
from .models import YearlyWorkload

from django.shortcuts import get_object_or_404
import numpy as np
import datetime
from django.contrib.auth.decorators import login_required
import os
import datetime

def tests(request):
    return HttpResponse(os.listdir("\\\\basfad.basf.net\\groups\\0050-BASF\\LUDWIGSHAFEN\\R\\GROUPS\\HM"))

@login_required()
def set_search_in(request):
    """ Adds the field search_in to the session object
    Args:
        request: The request object.
        sorting: The row in the database the list should be sorted by
    """
    if request.method == 'POST':
        request.session["search_in"] = request.POST.get("search_in")
        return HttpResponseRedirect(reverse_lazy('projects:project-list'))
    else:
        return HttpResponse(status=400)

@login_required()
def search(request):
    if request.method == 'POST':
        try:
            search_string = (request.POST["search_string"])
        except:
            return HttpResponse(status=400)

        projects = None
        if 'search_in' in request.session:
            if request.session['search_in'] == 'all_fields':
                projects = ResearchProject.objects.all()
            elif request.session['search_in'] == 'title':
                projects = ResearchProject.objects.filter(title__contains=search_string)
            elif request.session['search_in'] == 'tools':
                projects = ResearchProject.objects.filter(tools__contains=search_string)
            elif request.session['search_in'] == 'plant_name':
                projects = ResearchProject.objects.filter(plant_name__contains=search_string)
        else:
            projects = ResearchProject.objects.all()

        # Search in serialized data: Inefficient but simple and flexible ...
        projects = serializers.serialize( "python", projects, fields = public_labels.keys())
        pks = [p["pk"] for p in projects]
        fields = [p["fields"] for p in projects]
        columns = [list(v.keys()) for v in fields]
        rows = [list(v.values()) for v in fields]

        column_where = []
        found_in_row = []
        for l in rows:
            l_out = []
            found = False
            for item in l:
                if search_string.lower() in item.lower():
                    l_out.append(True)
                    found = True
                else:
                    l_out.append(False)
            column_where.append(l_out)
            found_in_row.append(found)

        results = [result for found, result in zip(found_in_row, projects) if found]
        column_where =  [result for found, result in zip(found_in_row, column_where) if found]

        context = {"columns":public_labels.values(), "projects": results}

        try:
            search_in_string = labels[request.session.get('search_in')]#labels is defined in forms.py and maps variable names to the string displayed in the GUI
        except:
            search_in_string = "all fields"

        context["search_in"] = search_in_string
        return render(request, 'projects/list.html', context)
    return HttpResponse("This route is only for POST requests",status=400)

class ProjectList(ListView):
    model = ResearchProject
    template_name = 'projects/list.html'
    context_object_name = 'projects'
    paginate_by = 5#This many items go on each page

    def set_sorting(request, sorting):
        """ Adds the field for sorting to the session object
        Args:
            request: The request object.
            sorting: The row in the database the list should be sorted by
        """
        request.session["project_list_sorting"] = sorting
        return HttpResponseRedirect(reverse_lazy('projects:project-list'))

    def get_queryset(self):
        try:
            query_set = ResearchProject.objects.order_by(Lower(self.request.session.get('project_list_sorting', 'title')))
            list(query_set)#evaluate and throw exception at this point if key for sorting is missing
            return query_set
        except Exception as e:
            return ResearchProject.objects.all()

    def get_context_data(self, **kwargs):
        """ Defines the context that is rendered as a list. Retrieves all projects from the database and
            returns all columns that correspond to public_labels keys. These columns are redered as the view.
            Pagination is used. Items are split such that this.paginate_by items are on each page.
        """
        context = super(ProjectList, self).get_context_data(**kwargs)
        projects = self.get_queryset()#model.objects.all()

        page = self.request.GET.get('page')
        paginator = Paginator(list(projects), self.paginate_by)#the paginator splits the projects (a list of dicts) into pages with this.paginate_by items on each page

        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)

        context['projects'] = serializers.serialize( "python", projects, fields = public_labels.keys())#Here we make sure to only display fields with public labels
        context["columns"] = public_labels.values

        try:
            search_in_string = labels[self.request.session.get('search_in')]#labels is defined in forms.py and maps variable names to the string displayed in the GUI
        except:
            search_in_string = "all fields"

        context["search_in"] = search_in_string
        return context

class EntryDelete(DeleteView):
    """ Simple Deleteview for ResearchProject """
    template_name = 'projects/delete.html'
    model = ResearchProject
    success_url = reverse_lazy('projects:project-list', args=[])

class ProjectEdit(UpdateView):
    template_name = 'projects/create.html'
    form_class= GeneralProjectInformation

    def get(self, request, *args, **kwargs):
        """ Processes get request. Returns Editview.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        try:#If a primary key was passed retrieve and display the values
            proj = ResearchProject.objects.get(pk=kwargs["pk"])
            form_helper = self.form_class(instance=proj)
            context = {'form': form_helper, "pk":proj.pk}
        except:#Create new empty form otherwise
            form_helper = self.form_class()
            context = {'form': form_helper}

        context["current_year"] = datetime.datetime.now().year
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Processes post request. Updates value in database according to primary key.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        try:#If a ResearchProject with the specified primary key exists already retrieve it such that it can be updated
            pk = self.kwargs["pk"]
            original = ResearchProject.objects.get(pk=pk)
            form = self.form_class(request.POST, instance= original)
        except:#Otherwise create a new form such that a new ResearchProject is created by form.save()
            form = self.form_class(request.POST)
        if form.is_valid():
            updated = form.save()
            updated.save()
            pk = updated.pk
            return self.redirect(pk)
        return render(request, self.template_name, {'project_letter_main': form})

    def redirect(self, pk = None):
        """ Returns the redirect after the form was successfully processed. Redirects to current page. Override for custom redirects.
        Args:
            pk: primary key.
        """
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))

class ProjectCreate(ProjectEdit):
    template_name = 'projects/create.html'
    form_class = GeneralProjectInformation

class ProjectEditFirst(ProjectEdit):
    template_name = 'projects/edit1.html'
    form_class = GeneralProjectInformation


class ProjectEditSecond(ProjectEdit):
    template_name = 'projects/edit2.html'
    form_class = AdditionalProjectInformation

class ProjectEditThird(UpdateView):
    template_name = 'projects/edit3.html'
    form_class = Workload

    def disable_past_month(self, form, form_year):
        month_names = list(form.fields.keys())
        now = datetime.datetime.now()

        month = now.month
        year = now.year
        day = now.day

        if form_year < year:
            for key in month_names:
                form.fields[key].required = False
                form.fields[key].widget.attrs['disabled'] = 'disabled'

        if form_year == year:
            for form_month in range(1,13):
                if form_month < month:
                    form.fields[month_names[form_month-1]].widget.attrs['disabled'] = 'true'
                    form.fields[month_names[form_month-1]].required = False
                if form_month == month and day > 4:
                    form.fields[month_names[form_month-1]].widget.attrs['disabled'] = 'true'
                    form.fields[month_names[form_month-1]].required = False
        return form

    def get(self, request, *args, **kwargs):
        """ Processes get request. Returns Editview.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        context = {}
        try:#If a primary key was passed (get parameter) retrieve and display the values
            pk = kwargs["pk"]
            year = kwargs["year"]
        except Exception as e:
            return HttpResponse(status=400)#otherwise it was a bad request

        research_project = get_object_or_404(ResearchProject, id = pk)

        try:#Get contributor instance. If user is not a contributor of the research project, return error view
            contributor = research_project.contributor_set.get(person=request.user)#find contributor
        except:
            return render(request, "projects/not_in_project_members_warning.html", {})

        try:#get values from database
            qs = YearlyWorkload.objects.filter(contributor = contributor)#retrieve all YearlyWorkload with ForeignKey == contributor
            qs = qs.filter(year = year)#Filter YearlyWorkload for current year
            yearly_workload = list(qs)[0]#select yearly_workload table for current year
            context['yearly_workload'] = yearly_workload
            form_helper = self.form_class(instance = yearly_workload)
        except:
            form_helper = self.form_class()#by default we return an empty form


        form_helper = self.disable_past_month(form_helper, year)

        now = datetime.datetime.now()

        context['form'] = form_helper
        context["research_project"] = research_project
        context["year"] = year
        context["current_year"] = year
        context["next_year"] = year+1
        context["previous_year"] = year-1

        context["maximal_budget"] = research_project.budget
        context["budget_share"] = contributor.budget_share
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        """ Processes post request. Updates value in database according to primary key.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        try:#If a primary key was passed (get parameter) retrieve and display the values
            pk = kwargs["pk"]
            year = kwargs["year"]
            budget_share = request.POST["budget_share"]#Additional value (input field not generated via createview)
        except Exception as e:
            return HttpResponse(status=400)#otherwise it was a bad request

        research_project = get_object_or_404(ResearchProject, id = pk)

        try:#we need the YearlyWorkload table that has a foreign key that relates to the project contributor
            contributor = research_project.contributor_set.get(person=request.user)#find contributor
        except:
            return HttpResponse("No such contributor", status=404)

        form = Workload(request.POST)#assume that we have to create a new Workload

        try:#Get workload from database for updating if it exists
            qs = YearlyWorkload.objects.filter(contributor = contributor)#retrieve all YearlyWorkload with ForeignKey == contributor
            qs = qs.filter(year = year)#Filter YearlyWorkload for current year
            yearly_workloads = list(qs)#select yearly_workload table for current year
            form = Workload(request.POST, instance = yearly_workloads[0])
        except:
            pass

        form = self.disable_past_month(form, year)#past month must be disabled (and required set to False) such that the form is valid.
        if form.is_valid():
            contributor.budget_share = budget_share
            contributor.save()
            yearly_workload = form.save(commit=False)#Do not save immediately
            yearly_workload.contributor = contributor#But save foreign key contributor first
            yearly_workload.year = year# and set year
            yearly_workload.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        #return render(request, self.template_name, {'project_letter_main': form})
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required()
def delete_work_time(request, pk):
    if request.method == "POST":
        obj = get_object_or_404(YearlyWorkload, id = pk)
        try:
            obj.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except Exception as e:
            return HttpResponse("Could not delete the specified work time model " + str(e),404)
    else:
        return HttpResponse("Bad request",400)
