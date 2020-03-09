from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy

from projects.models import *

from capacities.forms import *
import datetime
import numpy as np
from time import sleep

from django.contrib.auth.decorators import login_required
import plotly.offline as opy
import plotly.graph_objs as go

from django.shortcuts import get_object_or_404


@login_required(login_url='/login_required')
def set_year(request):
    """ Adds the field search_in to the session object
    Args:
        request: The request object.
        sorting: The row in the database the list should be sorted by
    """
    if request.method == 'POST':
        request.session["capacities_year"] = request.POST.get("year")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponse(status=400)

@login_required(login_url='/login_required')
def set_person(request):
    """ Adds the field search_in to the session object
    Args:
        request: The request object.
        sorting: The row in the database the list should be sorted by
    """
    if request.method == 'POST':
        request.session["capacities_person_id"] = request.POST.get("person_id")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponse(status=400)

def get_monthly_duty(person, year, yearly_duty=250000/12):
    keys = ["part_time_jan","part_time_feb","part_time_mar","part_time_apr","part_time_may","part_time_jun",
            "part_time_jul","part_time_aug","part_time_sep","part_time_oct","part_time_nov","part_time_dec"]
    part_time = WorkTimeModel.objects.filter(year = year, person = person)
    if len(list(part_time)) == 0:
        part_time = WorkTimeModel()
        part_time.year = year
        part_time.person = person
        for k in keys:
            setattr(part_time, k, person.default_work_time)
        part_time.save()
    else:
        part_time = part_time[0]
    percentages = []
    for k in keys:
        percentages.append(getattr(part_time, k))
    target_euros_per_month = yearly_duty*np.array(percentages)/100
    cumulative_target = np.cumsum(target_euros_per_month)
    return np.array(percentages), target_euros_per_month, cumulative_target

def get_key_figures(target_euros_per_month, monthly_workload):
    workload_across_projects = np.sum(monthly_workload,axis = 0)#per month across projects
    booking_ratio = (workload_across_projects/target_euros_per_month)*100
    surplus_current_month = workload_across_projects-target_euros_per_month
    cumulative_workload = np.cumsum(workload_across_projects)

    cumulative_target = np.cumsum(target_euros_per_month)
    year_goal = cumulative_target[-1]

    cumulative_booking_ratio_year_goal = (cumulative_workload/year_goal)*100
    burndown = ((np.array([year_goal for x in range(12)])-cumulative_workload)/year_goal)*100

    return workload_across_projects, cumulative_workload, surplus_current_month, booking_ratio, cumulative_booking_ratio_year_goal, burndown

def get_monthly_workload(yearly_workloads):
    # retrieve yearly workload for these projects
    keys = ["workload_jan","workload_feb","workload_mar","workload_apr","workload_may","workload_jun","workload_jul",
            "workload_aug","workload_sep","workload_oct","workload_nov","workload_dec"]

    monthly_workload = []# Collect values in a nested list of yearly workloads
    for load in yearly_workloads:
        workloads_for_current_project = []
        for k in keys:
            workloads_for_current_project.append(getattr(load, k))
        monthly_workload.append(workloads_for_current_project)
    monthly_workload = np.array(monthly_workload)
    return monthly_workload

@login_required(login_url='/login_required')
def group_capacities(request):
    context = {}
    users = Person.objects.all().exclude(is_superuser=True)
    year = request.session.get('capacities_year', datetime.datetime.now().year)
    context["selected_year"] = year

    capacity_per_month = {}
    for user in users:
        contributions = Contributor.objects.filter(person=user)#Get all contributions of a person
        yearly_workloads = YearlyWorkload.objects.filter(contributor__in = contributions, year=year)#get yearly workloads for current year
        monthly_workload = get_monthly_workload(yearly_workloads)
        percentages, target_euros_per_month, cumulative_target = get_monthly_duty(user, year)
        booking_ratio = get_key_figures(target_euros_per_month, monthly_workload)[3]
        capacity_per_month[user] = np.array(np.round(booking_ratio), dtype=np.int32)
    context["person_workload"] = capacity_per_month
    context["persons"] = users
    return render(request, 'capacities/capacities_group.html', context)

@login_required(login_url='/login_required')
def capacities(request):
    context = {}
    context["part_time"] = {}
    context["stats_workload"] = {}
    context["key_figures"] = {}
    context["persons"] = list(Person.objects.all().exclude(is_superuser=True))

    try:#Try retrieving values from the database ...
        year = request.session.get('capacities_year', datetime.datetime.now().year)
        person_id = request.session.get('capacities_person_id',context["persons"][0].id)
        person = Person.objects.get(id=person_id)#By default try person with pk = 1
        context["selected_year"] = year
        context["selected_person"] = person

        # retrieve a list of projects for the known year and person
        contributions = Contributor.objects.filter(person=person)#Get all contributions of a person
        yearly_workloads = YearlyWorkload.objects.filter(contributor__in = contributions, year=year)#get yearly workloads for current year
        projects = [load.contributor.research_project for load in yearly_workloads]

        if len(projects) == 0:
            return render(request, 'capacities/no_projects_warning.html', context)

        monthly_workload = get_monthly_workload(yearly_workloads)

        percentages, target_euros_per_month, cumulative_target = get_monthly_duty(person, year)
        workload_across_projects, cumulative_workload, surplus_current_month, booking_ratio, cumulative_booking_ratio_year, burndown = get_key_figures(target_euros_per_month, monthly_workload)

        context["part_time"]["Part time [%]"] = percentages
        context["part_time"]["Monthly target [k€] <br> (Part-time considered)"] = np.round(target_euros_per_month/1000)
        context["part_time"]["Cumulative target [k€]"] = np.array(np.round(cumulative_target/1000),dtype=np.int32)
        context["stats_workload"]["Workload across projects [k€] <br> (sum per month)"] = np.array(np.round(workload_across_projects/1000),dtype=np.int32)
        context["stats_workload"]["Cumulative workload [k€]"] = np.array(np.round(cumulative_workload/1000),dtype=np.int32)
        context["key_figures"]["Booking ratio per current month [%]"] = np.array(np.round(booking_ratio),dtype=np.int32)
        context["key_figures"]["Surplus for current month [k€]"] = np.array(np.round(surplus_current_month/1000),dtype=np.int32)
        context["key_figures"]["Cumulative booking ratio per year-goal [%]"] = np.array(np.round(cumulative_booking_ratio_year),dtype=np.int32)
        context["key_figures"]["Burndown [%]"] = np.array(np.round(burndown),dtype=np.int32)

    except Exception as e:
        projects = [[]]
        monthly_workload = []

    context["project_rows"] = list(zip(projects,monthly_workload))
    return render(request, 'capacities/capacities.html', context)

@login_required(login_url='/login_required')
def burndown(request):
    context = {}
    context["persons"] = Person.objects.all().exclude(is_superuser=True)

    try:#Try retrieving values from the database ...
        year = request.session.get('capacities_year', datetime.datetime.now().year)
        person_id = request.session.get('capacities_person_id',context["persons"][0].id)
        person = Person.objects.get(id=person_id)#By default try person with pk = 1
        context["selected_year"] = year
        context["selected_person"] = person

        # retrieve a list of projects for the known year and person
        contributions = Contributor.objects.filter(person=person)#Get all contributions of a person
        yearly_workloads = YearlyWorkload.objects.filter(contributor__in = contributions, year=year)#get yearly workloads for current year
        projects = [load.contributor.research_project for load in yearly_workloads]

        if len(projects) == 0:
            return render(request, 'capacities/no_projects_warning.html', context)

        monthly_workload = get_monthly_workload(yearly_workloads)
        target_euros_per_month = get_monthly_duty(person, year)[1]
        burndown = get_key_figures(target_euros_per_month, monthly_workload)[5]

    except Exception as e:
        return HttpResponse("No such capacity or person. " + str(e), 400)

    try:
        x = np.arange(len(burndown))#12 month
        y = np.array(burndown)
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10}, mode="lines",  name='1st Trace')
        layout=go.Layout(title="", xaxis={'title':'month', "tickvals" : list(range(12)),"ticktext":['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',"Jul","Aug","Sep","Oct","Nov","Dec"]},
                                    yaxis={'title':'remaining duties [%]','range':[-5,max(burndown)+5]})
        figure=go.Figure(data=trace1,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context["plot"] = div
    except Exception as e:
        print(e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    return render(request, 'capacities/burndown.html', context)