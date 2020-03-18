from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import *
import datetime
from lightweight_research_tool.settings import *
from pathlib import Path
import os
import pandas as pd
import calendar
import io


def exports(request):
    context = {}
    try:#Try retrieving values from the database ...
        year = request.session.get('capacities_year', datetime.datetime.now().year)
        person_id = request.session.get('capacities_person_id',list(Person.objects.filter(last_name__gt=''))[0].id)
        person = Person.objects.get(id=person_id)#By default try person with pk = 1
        context["selected_year"] = year
        context["selected_person"] = person
        context["persons"] = Person.objects.all().exclude(is_superuser=True)
        return render(request, 'exports/exports.html', context)
    except Exception as e:
        return HttpResponse("Invalid session status" + str(e), status=404)

def download_worktimes(request, year):
    worktimes = WorkTimeModel.objects.filter(year = year)
    worktimes = [[w.person,w.part_time_jan,w.part_time_feb,w.part_time_mar,
                  w.part_time_apr,w.part_time_may,w.part_time_jun,w.part_time_jul,
                  w.part_time_aug,w.part_time_sep,w.part_time_oct,w.part_time_nov, w.part_time_dec] for w in worktimes]
    columns = ["Group member"]
    columns.extend([calendar.month_abbr[(x%12)+1] for x in range(12)])
    df = pd.DataFrame(worktimes,columns=columns)
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='work_time_models', index=False)
    writer.save()
    xlsx_data = output.getvalue()
    response = HttpResponse(xlsx_data, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename="work_time_models_'+str(year)+'.xlsx"'
    return response


def download_database(request):
    with open(os.path.join(Path(BASE_DIR).parent,"database/db.sqlite3"), "rb") as f:
        response = HttpResponse(f.read(),content_type="application/x-sqlite3")
        response['Content-Disposition'] = 'attachment; filename="db.sqlite3"'
        return response
