from django.shortcuts import render
from django.core.context_processors import request
from ourplatform.models import *
from django.http import HttpResponse

# Create your views here.
def test(request):
    user = User(username="test3", password="123456")
    user.save()
    Activity(owner=user, starttime="2012-08-26", endtime="2012-08-26").save()
    Activity(owner=user, starttime="2012-08-27", endtime="2012-08-27").save()
    Joiner(activity=Activity.objects.get(id=1), user=User.objects.get(id=2)).save()
    return HttpResponse("Hello world")