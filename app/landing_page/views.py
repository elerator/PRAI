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
    """ View for the landing page.
    Args:
        request: Request object.
    Returns:
        HttpResponse: Rendered landing page.
    """
    return render(request, 'landing_page/landing.html', {})

token_to_info_url = 'https://app.roqs.basf.net/auth/token2info'
basf_login = "https://app.roqs.basf.net/auth/login.html"
redirect_uri = "https%3A%2F%2Fapp-dev.roqs.basf.net%2Fprai_information_desk%2Fafter_login"

def login_view(request):
    """ Method to redirect user to the BASF federation login.
        The redirect_uri is passed as get_request parameter andrefers to the route that corresponds to after_login.
    Args:
        request: Request object.
    Returns:
        HttpResponse: Redirect to BASF login or Bad Request message.
    """
    try:
        #user = Person.objects.filter(username__iexact="gerstem5")#Bypass basf auth
        #django_login(request, user[0])
        #return HttpResponseRedirect(request.GET["next"])

        next = request.GET["next"]
        url = basf_login + "?redirect_uri=" + redirect_uri
        url += "?next="
        url += quote(next, safe="")
        return HttpResponseRedirect(url)
    except:
        return HttpResponse("Bad Request",status=400)

def after_login(request):
    """ Authentification callback. This method is triggered after the authentification cookies were set by the federation login.
        Makes a request to token_to_info_url and checks whether the access token retrieved from cookies is a valid one.
    Args:
        request: Request object
    Returns:
        HttpResponseRedirect: Redirect to the redirect url (get request parameter)
    """
    try:
        redirect_url = request.GET["next"]
        auth_header = request.META
        cookie_federation_access_token = request.COOKIES.get('basf_federation_access_token')
        cookie_federation_cn = request.COOKIES.get('basf_federation_cn')
        r = requests.post(token_to_info_url, data={'token': cookie_federation_access_token}, verify=False, timeout=30)
        assert r.status_code == 200
        session_federation = r.json()

        if not 'error' in session_federation and session_federation['user_id'] == cookie_federation_cn:
            #User is authenticated
            user = Person.objects.filter(username__iexact=cookie_federation_cn)
            if user.exists():
                #User is member of production ai
                django_login(request, user[0])
                return HttpResponseRedirect(redirect_url)
        #User not authentificated or not member of production AI
        return HttpResponseRedirect(reverse_lazy("landing_page"))
    except Exception as e:
        #Something went wrong during authentification
        return HttpResponseRedirect(reverse_lazy("landing_page"))




def logout(request):
    """ Logs the user out
    Args:
        request: Request object
    Returns:
        HttpResponseRedirect: Redirect to landing page
    """
    django_logout(request)#TODO log out from BASF too (!?)
    return HttpResponseRedirect(reverse_lazy("landing_page"))

def login_required(request):
    """ View method that renders login required message.
    Args:
        request: Request object
    Returns:
        HttpResponse with rendered login required template or bad request message.
    """
    try:
        return render(request, 'landing_page/login_required.html', {"next":request.GET["next"]})
    except:
        return HttpResponse("Bad Request at login required: Next is " + request.GET["next"],status=400)
