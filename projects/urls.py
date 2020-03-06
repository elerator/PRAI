from django.urls import path

from . import views
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'projects'
urlpatterns = [
    path('list/', login_required(views.ProjectList.as_view(), login_url='/login_required'), name='project-list'),
    path('list/sortby/<str:sorting>', views.ProjectList.set_sorting, name="set_sorting"),
    path('list/search_in/', set_search_in, name="set_search_in"),
    path('list/search/', search, name="search"),
    path('create/', login_required(views.ProjectCreate.as_view(), login_url='/login_required'), name='create'),
    path('edit1/<int:pk>/', login_required(views.ProjectEditFirst.as_view(), login_url='/login_required'), name='edit1'),
    path('edit2/<int:pk>/', login_required(views.ProjectEditSecond.as_view(), login_url='/login_required'), name='edit2'),
    path('edit3/<int:pk>/<int:year>', login_required(views.ProjectEditThird.as_view(), login_url='/login_required'), name='edit3'),
    path('delete/<int:pk>/', login_required(views.EntryDelete.as_view(), login_url='/login_required'), name='entry_delete'),
    path('delete_workload/<int:pk>', login_required(delete_work_time, login_url='/login_required'), name='delete_workload' )
]
