from django.urls import path

from landing_page.views import *

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login_page', login_view, name="login_page"),
    path('logout', logout, name="logout"),
    path('login_required', login_required, name="login_required"),
    path('login', login, name='login'),
    path('after_login/<str:sorting>', after_login, name="after_login")
]
