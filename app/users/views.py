from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core import serializers
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

from .forms import *

class UserList(ListView):
    model = Person
    template_name = 'users/user_list.html'
    context_object_name = 'person'

    def get_queryset(self):
        try:
            query_set = Person.objects.all()
            list(query_set)#evaluate and throw exception at this point if key for sorting is missing
            return query_set
        except Exception as e:
            return Person.objects.all()

    def get_context_data(self, **kwargs):
        """ Defines the context that is rendered as a list. Retrieves all projects from the database and
            returns all columns that correspond to public_labels keys. These columns are redered as the view.
            Pagination is used. Items are split such that this.paginate_by items are on each page.
        """
        context = super(UserList, self).get_context_data(**kwargs)
        persons = self.get_queryset()#model.objects.all()
        persons = persons.filter(is_superuser=False)#remove superuser from list

        context['persons'] = serializers.serialize( "python", persons, fields = ["first_name","last_name"])#
        context["columns"] = ["First Name","Name"]
        return context

class PersonWorkTime(UpdateView):
    template_name = 'users/edit2.html'
    form_class = WorkTime

    def set_default(self, form, person):
        keys = list(form.fields.keys())
        for k in keys:
            form.fields[k].initial = person.default_work_time
        return form

    def get(self, request, *args, **kwargs):
        """ Processes get request. Returns Editview.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        context = {}
        try:#If a primary key was passed (get parameter) retrieve and display the values
            pk = kwargs["pk"]
            year = kwargs["year"]
            person = get_object_or_404(Person, id = pk)
        except Exception as e:
            return HttpResponse(status=400)#otherwise it was a bad request

        try:#get values from database
            qs = WorkTimeModel.objects.filter(year = year, person = person)#retrieve all YearlyWorkload with ForeignKey == contributor
            worktimes = list(qs)[0]#select yearly_workload table for current year
            context["worktimes"] = worktimes
            form_helper = self.form_class(instance = worktimes)
        except:
            form_helper = self.set_default(self.form_class(), person)

        context['form'] = form_helper
        context["pk"] = pk
        context["year"] = year
        context["current_year"] = datetime.datetime.now().year
        context["previous_year"] = year -1
        context["next_year"] = year + 1

        context["person"] = person
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Processes post request. Updates value in database according to primary key.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        try:#If a primary key was passed (get parameter) retrieve and display the values
            pk = kwargs["pk"]
            year = kwargs["year"]
            person = get_object_or_404(Person, id = pk)
        except Exception as e:
            return HttpResponse(status=400)#otherwise it was a bad request

        try:#Get WorkTime from database for updating if it exists
            qs = WorkTimeModel.objects.filter(year = year, person = person)
            form = WorkTime(request.POST, instance = list(qs)[0])
        except Exception as e:
            form = WorkTime(request.POST)#assume that we have to create a new WorkTime

        if form.is_valid():
            work_time_model = form.save(commit=False)#Do not save immediately
            work_time_model.person = person#But save foreign key contributor first
            work_time_model.year = year# and set year
            work_time_model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class UserEditMain(UpdateView):
    template_name = 'users/edit1.html'
    form_class= PersonForm

    def get(self, request, *args, **kwargs):
        """ Processes get request. Returns Editview.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        try:#If a primary key was passed retrieve and display the values
            person = Person.objects.get(pk=kwargs["pk"])
            form = self.form_class(instance=person)
            context = {'form': form, "person":person, "current_year":datetime.datetime.now().year}
        except Exception:
            return HttpResponse("Bad request", status=400)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Processes post request. Updates value in database according to primary key.
        Args:
            *args: List of args
            **kwargs: Dictionary with key value pairs of arguments. Must contain the primary key "pk".
            request: Request object
        """
        try:#If a ResearchProject with the specified primary key exists already retrieve it such that it can be updated
            pk = self.kwargs["pk"]
            person = Person.objects.get(pk=kwargs["pk"])
            form = self.form_class(request.POST, instance=person)
        except Exception as e:
            return HttpResponse("Person with the specified pk does not exist", status=400)
        if form.is_valid():
            updated = form.save()
            updated.save()
            pk = updated.pk
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, self.template_name, {'form': form,'person':person})

class UserCreate(CreateView):
    template_name = 'users/create.html'
    form_class= PersonCreateForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        qs = Person.objects.filter(username = username)
        if qs.count() >= 1:
            return render(request, "users/user_already_exists.html",{})
        return super(UserCreate, self).post(request, *args, **kwargs)
        '''
        user = Person()
        user.username = username
        user.save()
        return HttpResponseRedirect(reverse_lazy("users:user_list",args=[]))'''

class DeleteUser(DeleteView):
    """ Simple Deleteview for ResearchProject """
    template_name = 'users/delete.html'
    model = Person
    success_url = reverse_lazy('users:user_list', args=[])

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, "users/superuser_required.html")
        return super(DeleteUser, self).post(request, *args, **kwargs)


@login_required()
def delete_work_time(request, pk):
    if request.method == "POST":
        obj = get_object_or_404(WorkTimeModel, id = pk)
        try:
            obj.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except Exception as e:
            return HttpResponse("Could not delete the specified work time model " + str(e),404)
    else:
        return HttpResponse("Bad request",400)
