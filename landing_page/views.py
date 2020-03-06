from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse
from users.models import Person
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse_lazy
from django.contrib.auth import logout as django_logout

import os

def landing_page(request):
    print("------------------------")
    print(os.listdir())
    return render(request, 'landing_page/landing.html', {})
    #os.system("python manage.py collectstatic --noinput")
    #return HttpResponse(str(os.listdir("./static")))

def login_view(request):
    try:
        return render(request, 'landing_page/login_page.html', {"next":request.GET["next"]})
    except:
        return HttpResponse("Bad Request",status=400)

def basf_authentification(basf_username, password):
    return True

def login(request):
    if request.method == 'POST':
        try:
            if basf_authentification(request.POST["username"],request.POST["password"]):
                try:
                    user = Person.objects.filter(username=request.POST["username"])[0]
                    django_login(request, user)
                    return HttpResponseRedirect(request.POST["next"])
                except Exception:
                    return render(request, 'landing_page/login_page.html', {"errors":True})
            else:
                return render(request, 'landing_page/login_page.html', {"errors":True,"next":request.POST["next"]})
        except MultiValueDictKeyError:#TODO the only exception type of relevance?
            return HttpResponse("Bad Request",status=400)
    else:
        return HttpResponse("Bad Request",status=400)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse_lazy("landing_page"))

def login_required(request):
    try:
        return render(request, 'landing_page/login_required.html', {"next":request.GET["next"]})
    except:
        return HttpResponse("Bad Request",status=400)
