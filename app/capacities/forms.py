from django import forms
from projects.models import *

class Workload(forms.ModelForm):
    """ Makes Model accessible for use in child classes of CreateView/UpdateView. """
    workload_jan = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_feb = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_mar = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_apr = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_may = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_jun = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_jul = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_aug = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_sep = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_oct = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_nov = forms.IntegerField(required=False, min_value=0, initial=0, label="")
    workload_dec = forms.IntegerField(required=False, min_value=0, initial=0, label="")

    class Meta:
        model = YearlyWorkload
        fields = []
        widgets = {
            'workload_jan': forms.NumberInput(attrs={'class':'form-control'}),
        }
