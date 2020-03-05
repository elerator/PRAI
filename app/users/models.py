from django.db import models
from projects.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.contrib.auth.decorators import login_required

class Person(AbstractUser):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000,null=True,blank=True)
    status = models.CharField(max_length=8, choices=(("active","active member of the group"),("inactive","former member of the group")), default='active')

    default_work_time = models.PositiveIntegerField(null=True, default = 80, validators=[MinValueValidator(0), MaxValueValidator(100)])
    def __str__(self):
        return self.first_name + " " + self.last_name

class WorkTimeModel(models.Model):
    year = models.PositiveIntegerField()

    part_time_jan = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_feb = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_mar = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_apr = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_may = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_jun = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_jul = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_aug = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_sep = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_oct = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_nov = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    part_time_dec = models.PositiveIntegerField(default=80.0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
