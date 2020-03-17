from django.urls import path

from . import views
from .views import *

app_name = 'exports'
urlpatterns = [
    path('', exports, name='exports'),
    path('download_database', download_database, name="download_database")
]
