from django.shortcuts import render
from django.core.context_processors import request
from ourplatform.models import *
from django.http import HttpResponse
from urllib2 import Request
import json

# Create your views here.
# def test(request):
#     user = User(username="test3", password="123456")
#     user.save()
#     Activity(owner=user, starttime="2012-08-26", endtime="2012-08-26").save()
#     Activity(owner=user, starttime="2012-08-27", endtime="2012-08-27").save()
#     Joiner(activity=Activity.objects.get(id=1), user=User.objects.get(id=2)).save()
#     return HttpResponse("Hello world")

def createActivities(request):
    userid = request.POST['uid']
    buf = User.objects.get(id=userid)
    newActivity = Activity(owner=buf, starttime=request.POST['starttime'], endtime=request.POST['endtime'], discription=request.POST['description'])
    newActivity.save()
    returnData = {'aid': newActivity.id, 
                  'uid': newActivity.owner.id, 
                  'starttime': newActivity.starttime,
                  'endtime': newActivity.endtime,
                  'description': newActivity.description}
    return HttpResponse(json.dumps(returnData, ensure_ascii=False))

def getActivities(request):
    listOfActivities = Activity.objects.all()
    returnData = []
    for i in listOfActivities:
        buf = {'aid': i.id,
               'uid': i.owner.id,
               'starttime': i.starttime,
               'endtime': i.endtime,
               'description': i.description
               }
        returnData.append(buf)
    return HttpResponse(json.dumps(returnData, ensure_ascii=False))

def getActivityById(request):
    aid = request.GET['id']
    arr = Activity.objects.filter(id=aid)
    acbuf = arr[0]
    returnData = {'aid': acbuf.id,
                  'uid': acbuf.owner.id,
                  'starttime': acbuf.starttime,
                  'endtime': acbuf.endtime,
                  'description': acbuf.description}
    return HttpResponse(json.dumps(returnData, ensure_ascii=False))
    
    
    
    