from django.urls import path

from . import views
from .views import *

app_name = 'kanban'
urlpatterns = [
    path('', kanban, name='kanban'),
    path('move_project_to',move_project_to,name="move_project_to")
]
