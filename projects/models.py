import datetime
from django.db import models
from users.models import *

def only_filename(instance, filename):
    return filename

class ResearchProject(models.Model):
    title = models.CharField(max_length=1000)
    project_partner = models.CharField(max_length=1000)
    goal = models.CharField(max_length=1000)
    milestones = models.CharField(max_length=1000)
    short_description = models.CharField(max_length=1000)
    plant_name = models.CharField(max_length=1000)
    funding = models.CharField(max_length=1000)
    tools = models.CharField(max_length=1000)
    budget = models.PositiveIntegerField()
    funding_type = models.CharField(max_length=3, choices=(("kdc","KDC"),("ktc","KTC"),("od","OD")), default='kdc')

    project_leader = models.CharField(max_length=1000)

    report = models.CharField(max_length=1000)

    start = models.DateField()
    end = models.DateField()
    cost_center = models.CharField(max_length=1000)

    project_stage = models.CharField(max_length=17, choices=(("planned","planned"),("started","started"),("modeling_complete","modeling complete"),("report_finished","report finished")), default='planned')
    contributors = models.ManyToManyField(Person, through='Contributor')

    def __str__(self):
        return self.title

class Contributor(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    budget_share = models.PositiveIntegerField(null=True)

class YearlyWorkload(models.Model):
    year = models.PositiveIntegerField()

    workload_jan = models.PositiveIntegerField(default=0,null=True)
    workload_feb = models.PositiveIntegerField(default=0,null=True)
    workload_mar = models.PositiveIntegerField(default=0,null=True)
    workload_apr = models.PositiveIntegerField(default=0,null=True)
    workload_may = models.PositiveIntegerField(default=0,null=True)
    workload_jun = models.PositiveIntegerField(default=0,null=True)
    workload_jul = models.PositiveIntegerField(default=0,null=True)
    workload_aug = models.PositiveIntegerField(default=0,null=True)
    workload_sep = models.PositiveIntegerField(default=0,null=True)
    workload_oct = models.PositiveIntegerField(default=0,null=True)
    workload_nov = models.PositiveIntegerField(default=0,null=True)
    workload_dec = models.PositiveIntegerField(default=0,null=True)

    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE,
        related_name='research_projects'
    )
