from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.http import HttpResponseRedirect, HttpResponse
from users.models import Person
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse_lazy
from django.contrib.auth import logout as django_logout
from urllib.parse import quote, unquote
import os
import requests

def landing_page(request):
    return render(request, 'landing_page/landing.html', {})

token_to_info_url = 'https://app.roqs.basf.net/auth/token2info'
post_basf_login_callback = "https://app.roqs.basf.net/auth/login.html?redirect_uri=https%3A%2F%2Fapp-dev.roqs.basf.net%2Fprai_information_desk%2Fafter_login"

def login_view(request):
    try:
        #user = Person.objects.filter(username__iexact="gerstem5")#Bypass basf auth
        #django_login(request, user[0])
        #return HttpResponseRedirect(request.GET["next"])

        next = request.GET["next"]
        url = post_basf_login_callback
        url += "?next="
        url += quote(next, safe="")
        return HttpResponseRedirect(url)
    except:
        return HttpResponse("Bad Request",status=400)

def after_login(request):
    redirect_url = request.GET["next"]
    auth_header = request.META
    cookie_federation_access_token = request.COOKIES.get('basf_federation_access_token')
    cookie_federation_cn = request.COOKIES.get('basf_federation_cn')
    r = requests.post(token_to_info_url, data={'token': cookie_federation_access_token}, verify=False, timeout=30)
    #assert r.status_code == 200
    session_federation = r.json()

    if not 'error' in session_federation and session_federation['user_id'] == cookie_federation_cn:
        #User is authenticated
        user = Person.objects.filter(username__iexact=cookie_federation_cn)
        if user.exists():
            #User is member of production ai
            django_login(request, user[0])
            return HttpResponseRedirect(redirect_url)

    # authentication failed: Go back to login
    url = post_basf_login_callback
    url += "?next="
    url += quote(redirect_url, safe="")
    return HttpResponseRedirect(url)


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse_lazy("landing_page"))

def login_required(request):
    try:
        return render(request, 'landing_page/login_required.html', {"next":request.GET["next"]})
    except:
        return HttpResponse("Bad Request at login required: Next is " + request.GET["next"],status=400)
