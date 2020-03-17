from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import *
import datetime
from lightweight_research_tool.settings import *
from pathlib import Path
import os


def exports(request):
    context = {}
    try:#Try retrieving values from the database ...
        year = request.session.get('capacities_year', datetime.datetime.now().year)
        person_id = request.session.get('capacities_person_id',list(Person.objects.filter(last_name__gt=''))[0].id)
        person = Person.objects.get(id=person_id)#By default try person with pk = 1
        context["selected_year"] = year
        context["selected_person"] = person
        return render(request, 'exports/exports.html', context)
    except Exception as e:
        return HttpResponse("Invalid session status" + str(e), status=404)


def download_database(request):
    with open(os.path.join(Path(BASE_DIR).parent,"database/db.sqlite3"), "rb") as f:
        response = HttpResponse(f.read(),content_type="application/x-sqlite3")
        response['Content-Disposition'] = 'attachment; filename="db.sqlite3"'
        return response
