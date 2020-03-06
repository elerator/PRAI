from django.urls import path
from capacities.views import *

app_name = 'capacities'
urlpatterns = [
    path('', capacities, name='capacities'),
    path('set_year',set_year, name='capacities_set_year'),
    path('set_person',set_person, name='capacities_set_person'),
    path('burndown',burndown, name="burndown"),
    path('group_capacities', group_capacities, name='group_capacities'),
]
