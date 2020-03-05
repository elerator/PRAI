from .models import *
from django import forms

class PersonForm(forms.ModelForm):
    """ Makes Model accessible for use in UpdateView """
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['username'].disabled = True

    class Meta:
        model = Person
        fields = ["first_name","last_name","username","default_work_time","status"]
        labels = {"default_work_time":"Default work time [%]"}
        help_texts = {
            'username': None,
        }

class PersonCreateForm(forms.ModelForm):
    """ Makes Model accessible for use in CreateView """

    class Meta:
        model = Person
        fields = ["first_name","last_name","username","default_work_time","status"]
        labels = {"default_work_time":"Default work time [%]"}
        help_texts = {
            'username': None,
        }


class WorkTime(forms.ModelForm):
    """ Makes Model accessible for use in child classes of CreateView/UpdateView. """
    part_time_jan = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for January [%]")
    part_time_feb = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for February [%]")
    part_time_mar = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for March [%]")
    part_time_apr = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for April [%]")
    part_time_may = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for May [%]")
    part_time_jun = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for June [%]")
    part_time_jul = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for July [%]")
    part_time_aug = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for August [%]")
    part_time_sep = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for September [%]")
    part_time_oct = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for October [%]")
    part_time_nov = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for Novemeber [%]")
    part_time_dec = forms.IntegerField(required=False, min_value=0, max_value=100, label="Work time for December [%]")

    class Meta:
        model = WorkTimeModel
        exclude = ["person","year"]
