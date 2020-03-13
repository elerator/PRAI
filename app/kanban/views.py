from django.shortcuts import render
from projects.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

@login_required()
def kanban(request):
    context = {}

    context["persons"] = Person.objects.all().exclude(is_superuser=True)
    year = request.session.get('capacities_year', datetime.datetime.now().year)
    context["selected_year"] = year

    person_id = request.session.get('capacities_person_id',context["persons"][0].id)
    person = Person.objects.get(id=person_id)#By default try person with pk = 1
    context["selected_person"] = person

    # retrieve a list of projects for the known year and person
    contributions = Contributor.objects.filter(person=person)#Get all contributions of a person
    yearly_workloads = YearlyWorkload.objects.filter(contributor__in = contributions, year = year)
    projects = [load.contributor.research_project for load in yearly_workloads]

    context["planned"] = [p for p in projects if p.project_stage == "planned"]
    context["started"] = [p for p in projects if p.project_stage == "started"]
    context["modeling_complete"] = [p for p in projects if p.project_stage == "modeling_complete"]
    context["report_finished"] = [p for p in projects if p.project_stage == "report_finished"]
    return render(request, 'kanban/kanban.html', context)

@login_required(login_url='/login_required')
def move_project_to(request):
    if request.method == "POST":
        project_stage = request.POST.get("project_stage")
        research_project_pk = request.POST.get("research_project_pk")
        if project_stage not in ["planned", "started", "modeling_complete", "report_finished"]:
            return HttpResponse("Bad request. No such project stage.", status= 400)
        obj = get_object_or_404(ResearchProject, id=research_project_pk)
        obj.project_stage = project_stage
        obj.save()
        return HttpResponse(200)
    else:
        return HttpResponse("Bad request",400)
