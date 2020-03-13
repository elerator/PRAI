from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse
from users.models import Person
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse_lazy
from django.contrib.auth import logout as django_logout
from urllib.parse import quote, unquote
import os
from basf_auth import check_authentication

def landing_page(request):
    return render(request, 'landing_page/landing.html', {})

def check_auth(request):
    session_federation = session.get('basf_federation')
    cookie_federation_cn = request.cookies.get('basf_federation_cn')
    cookie_federation_access_token = request.cookies.get('basf_federation_access_token')
    auth_header = request.headers.get('Authorization')
    auth_result = basf_auth.check_authentication(session_federation, cookie_federation_cn, cookie_federation_access_token, auth_header)
    if auth_result:
        session['basf_federation'] = auth_result

    return auth_result

def login_view(request):
    try:
        next = request.GET["next"]
        url = "https://app.roqs.basf.net/auth/login.html?redirect_uri=https%3A%2F%2Fapp-dev.roqs.basf.net%2Fprai_information_desk%2Fafter_login"
        url += "?next="
        url += quote(next, safe="")
        return HttpResponseRedirect(url)
    except:
        return HttpResponse("Bad Request",status=400)

def after_login(request):
    redirect_url = request.GET["next"]
    return HttpResponse(request.COOKIES.get('basf_federation_logged_in'))
    #return HttpResponseRedirect(redirect_url)

def login(request):
    return login_view(request)
    """
    if request.method == 'POST':
        try:
            if basf_authentification(request.POST["username"],request.POST["password"]):
                try:
                    user = Person.objects.filter(username=request.POST["username"])[0]
                    django_login(request, user)
                    return HttpResponseRedirect(request.POST["next"])
                except Exception as e:
                    #return render(request, 'landing_page/login_page.html', {"errors":True})
                    return HttpResponse(str(e))
            else:
                return render(request, 'landing_page/login_page.html', {"errors":True,"next":request.POST["next"]})
        except MultiValueDictKeyError:#TODO the only exception type of relevance?
            return HttpResponse("Bad Request",status=400)
    else:
        return HttpResponse("Bad Request",status=400)"""

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse_lazy("landing_page"))

def login_required(request):
    try:
        return render(request, 'landing_page/login_required.html', {"next":request.GET["next"]})
    except:
        return HttpResponse("Bad Request at login required: Next is " + request.GET["next"],status=400)
