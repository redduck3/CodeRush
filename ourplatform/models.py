from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    gender = models.BooleanField(default = True)
    
class Activity(models.Model):
    owner = models.ForeignKey(User)
    starttime = models.DateField()
    endtime = models.DateField()
    kind = models.IntegerField()
    description = models.CharField(max_length=140)
    
class Joiner(models.Model):
    activity = models.ForeignKey(Activity)
    user = models.ForeignKey(User)