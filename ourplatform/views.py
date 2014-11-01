from django.shortcuts import render
from django.core.context_processors import request
from ourplatform.models import *
from django.http import *
from urllib2 import Request
import json
from datetime import datetime

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

def getActivityById(request, id):
    aid = id
    arr = Activity.objects.filter(id=aid)
    acbuf = arr[0]
    returnData = {'aid': acbuf.id,
                  'uid': acbuf.owner.id,
                  'starttime': acbuf.starttime,
                  'endtime': acbuf.endtime,
                  'description': acbuf.description}
    return HttpResponse(json.dumps(returnData, ensure_ascii=False))

def getActivitiesUndo(request):
    listOfActivities = Activity.objects.all()
    returnData = []
    for i in listOfActivities:
        if (i.endtime <= datetime.now()):
            buf = {'aid': i.id,
               'uid': i.owner.id,
               'starttime': i.starttime,
               'endtime': i.endtime,
               'description': i.description
               }
            returnData.append(buf)
    return HttpResponse(json.dumps(returnData, ensure_ascii=False))
    
def updateActivity(request, aid):
    userBuf = User.objects.filter(id=request.PUT['uid'])[0]
    myactivity = Activity.objects.get(id=aid)
    myactivity.owner = userBuf
    myactivity.starttime = request.POST['starttime']
    myactivity.endtime = request.POST['endtime']
    myactivity.description = request.POST['description']
    myactivity.save()
    return HttpResponse()
    
def login(request):
    payload_json = request.POST['payload']
    payload = json.load(payload_json)
    postname = payload['username']
    postpasswd = payload['password']
    
    result = User.objects.filter(username = postname,password = postpasswd)
    if len(result) == 0:
        response = HttpResponse()
        '''modify status'''
        return response
    user = result[0]
    '''
    request.session["uid"] = user.id
    request.session["username"] = user.username
    request.session["password"] = user.password
    request.session["gender"] = user.gender
    '''
    request.session['user'] = user
    return HttpResponse("OK")

def logout(request):
    try:
        '''
        del request.session['uid']
        del request.session['username']
        del request.session['password']
        del request.session['gender']
        '''
        del request.session['user']
    except KeyError:
        pass
    return HttpResponse("OK")
    
        
    
def createUser(request):
    payload_json = request.POST['payload']
    payload = json.load(payload_json)
    postname = payload['username']
    postpasswd = payload['password']
    postgender = payload['gender']

    result = User.objects.filter(username = postname)
    if len(result)!= 0:
        return HttpResponseBadRequest('%s has already been registered!' % postname)
    
    user = User(postname,postpasswd,postgender)
    user.save()
    response = {}
    response['uid'] = user.id
    response['username'] = user.username
    response_json = json.dumps(response)
    '''
    request.session["uid"] = user.id
    request.session["username"] = user.username
    request.session["password"] = user.password
    request.session["gender"] = user.gender
    '''
    request.session['user'] = user
    
    return HttpResponse(response_json)

def getUser(request):
    getid = request.GET['id']
    user = User.objects.get(id = getid)
    if len(user) == 0:
        return HttpResponseBadRequest()
    response = {}
    response['uid'] = user.id
    response['username'] = user.username
    response['password'] = user.password
    response['gender'] = user.gender
    response_json = json.dumps(response)
    return HttpResponse(response_json)

def updateUser(request):
    if 'uid' not in request.session:
        response = HttpResponse()
        '''modify status'''
        return response
    uid = request.session['uid']
    putid = request.POST['id']
    if uid != putid:
        return HttpResponseForbidden()
    result = User.objects.filter(id = putid)
    if len(result) == 0:
        return HttpResponseBadRequest('does not exist')
    user = result[0]
    payload_json = request.PUT['payload']
    payload = json.load(payload_json)
    user.username = payload['username']
    user.password = payload['password']
    user.gender = payload['gender']
    user.save()
    return HttpResponse('OK')

def deleteUser(request):
    if 'user' not in request.session:
        response = HttpResponse()
        '''modify status'''
        return response
    uid = request.session['user'].id
    getid = request.POST['id']
    if uid !=getid:
        return HttpResponseForbidden()
    result = User.objects.filter(id = getid)
    if len(result) == 0:
        return HttpResponseBadRequest('does not exist')
    user = result[0]
    user.delete()
    try:
        '''
        del request.session['uid']
        del request.session['username']
        del request.session['password']
        del request.session['gender']
        '''
        del request.session['user']
    except KeyError:
        pass
    return HttpResponse('OK')

    
    
    