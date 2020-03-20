from django.urls import path

from . import views
from .views import *

app_name = 'exports'
urlpatterns = [
    path('', exports, name='exports'),
    path('download_database', download_database, name="download_database"),
    path('download_worktimes/<int:year>', download_worktimes, name="download_worktimes"),
    path('download_projects/', download_projects, name="download_projects"),
]
