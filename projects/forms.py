from django import forms
from .models import *

public_labels = {#attributes and their respective labels that can be seen by any authentificated user. Budget etc are ommitted here.
    "title": "Product or project Title",
    "project_partner" : "Originator(s) and project partners ",
    "goal" : "Goal and motivation",
    "milestones" : "Milestones and targeted outcome/transfer",
    "short_description" : "Short work description",
    "plant_name" : "Plant or process name",
    "funding" : "Funding source / customer",
    "tools" : "Methods and tools",
}

private_labels = {
}

labels = {**public_labels, **private_labels}

class GeneralProjectInformation(forms.ModelForm):
    """ Makes Model accessible for use in child classes of CreateView/UpdateView. """
    product_name = forms.CharField(required=False, initial="")#Add initial values here

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields["contributors"].queryset = self.fields["contributors"].queryset.exclude(last_name="")#Remove empty choice i.e. superuser

    class Meta:
        model = ResearchProject
        fields = ["title","contributors","goal","short_description","plant_name",
                    "funding","tools","budget","project_leader","start","end"]
        labels = labels

        widgets = {
            'start': forms.TextInput(attrs={'type': 'date'}),#set the type of of the input fields
            'end': forms.TextInput(attrs={'type': 'date'})
        }

class AdditionalProjectInformation(forms.ModelForm):
    """ Makes Model accessible for use in child classes of CreateView or UpdateView. """
    class Meta:
        model = ResearchProject
        fields = ["cost_center","project_partner","project_stage","milestones","funding_type"]
        labels = labels

class Workload(forms.ModelForm):
    """ Makes Model accessible for use in child classes of CreateView/UpdateView. """
    workload_jan = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for January")
    workload_feb = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for February")
    workload_mar = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for March")
    workload_apr = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for April")
    workload_may = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for May")
    workload_jun = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for June")
    workload_jul = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for July")
    workload_aug = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for August")
    workload_sep = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for September")
    workload_oct = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for October")
    workload_nov = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for November")
    workload_dec = forms.IntegerField(required=True, min_value=0, initial=0, label="Workload for December")

    class Meta:
        model = YearlyWorkload
        exclude = ("research_project","year","contributor")
        labels = labels
