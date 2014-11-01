from django.shortcuts import render
from django.core.context_processors import request
from ourplatform.models import *
from django.http import *
from urllib2 import Request
import json
from datetime import datetime, date
from ourplatform import CJsonEncoder
from django.core.serializers.json import DjangoJSONEncoder
from distutils.tests.test_archive_util import UID_GID_SUPPORT

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
    return HttpResponse(json.dumps(returnData, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")

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
    return HttpResponse(json.dumps(returnData, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")

def getActivityById(request, id):
    aid = id
    arr = Activity.objects.filter(id=aid)
    acbuf = arr[0]
    returnData = {'aid': acbuf.id,
                  'uid': acbuf.owner.id,
                  'starttime': acbuf.starttime,
                  'endtime': acbuf.endtime,
                  'description': acbuf.description}
    return HttpResponse(json.dumps(returnData, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")

def getActivitiesUndo(request):
    listOfActivities = Activity.objects.all()
    returnData = []
    for i in listOfActivities:
        if (i.endtime >= date.today()):
            buf = {'aid': i.id,
               'uid': i.owner.id,
               'starttime': i.starttime,
               'endtime': i.endtime,
               'description': i.description
               }
            returnData.append(buf)
    return HttpResponse(json.dumps(returnData, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")
    
def updateActivity(request, aid):
    userBuf = User.objects.filter(id=request.PUT['uid'])[0]
    myactivity = Activity.objects.get(id=aid)
    myactivity.owner = userBuf
    myactivity.starttime = request.POST['starttime']
    myactivity.endtime = request.POST['endtime']
    myactivity.description = request.POST['description']
    myactivity.save()
    return HttpResponse('ok')
    
def login(request):
    payload_json = request.POST['payload']
    payload = json.load(payload_json)
    postname = payload['username']
    postpasswd = payload['password']
    
    result = User.objects.filter(username = postname,password = postpasswd)
    if len(result) == 0:
        return HttpResponse(status = 401)
    user = result[0]
    '''
    request.session["uid"] = user.id
    request.session["username"] = user.username
    request.session["password"] = user.password
    request.session["gender"] = user.gender
    '''
    request.session['user'] = user
    requestContext = {}
    requestContext['uid'] = user.id
    requestContext['username'] = user.username
    return HttpResponse(json.dumps(requestContext),content_type="application/json")

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
    
    return HttpResponse(response_json,content_type="application/json")

def getUser(request,id):
    getid = id
    users = User.objects.filter(id = getid)
    if len(users) == 0:
        return HttpResponseBadRequest()
    user = users[0]
    response = {}
    response['uid'] = user.id
    response['username'] = user.username
    response['password'] = user.password
    response['gender'] = user.gender
    response_json = json.dumps(response)
    return HttpResponse(response_json,content_type="application/json")

def updateUser(request,id):
    if 'user' not in request.session:
        return HttpResponse(status = 401)
    uid = request.session['user'].id
    putid = id
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
    
    request.session['user'] = user
    
    return HttpResponse('OK')

def deleteUser(request,id):
    if 'user' not in request.session:
        return HttpResponse(status = 401)
    uid = request.session['user'].id
    getid = id
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

def createJoiner(request):
    if 'user' not in request.session:
        return HttpResponse(status = 401)
    userid = request.session['user'].id
    payload_json = request.POST['payload']
    payload = json.load(payload_json)
    postaid = payload['aid']
    postuid = payload['uid']
    if userid!=postuid:
        return HttpResponseForbidden()
    joiners = Joiner.objects.filter(aid = postaid, uid = postuid)
    if len(joiners) != 0:
        return HttpResponseBadRequest()
    try:
        activity = Activity.objects.get(id = postaid)
        user = User.objects.get(id = postuid)
        joiner = Joiner(activity,user)
        joiner.save()
        response = {}
        response['jid'] = joiner.id
        return HttpResponse(json.dumps(response),content_type="application/json")
    except Exception:
        return HttpResponseBadRequest()

def deleteJoiner(request,aid):
    if 'user' not in request.session:
        return HttpResponse(status = 401)
    userid = request.session['user'].id

    joiners = Joiner.objects.filter(aid = aid, uid = userid)
    if len(joiners) == 0:
        return HttpResponseBadRequest()
    joiner = joiners[0]
    joiner.delete()
    return HttpResponse()

def getJoinersByUser(request,uid):
    if 'user' not in request.session:
        return HttpResponse(status = 401)
    userid = request.session['user'].id
    if userid != uid:
        return HttpResponseForbidden()
    joiners = Joiner.objects.filter(uid = uid)
    returnData = []
    for joiner in joiners:
        activity = joiner.activity
        buf = {'aid': activity.id,
               'uid': activity.owner.id,
               'starttime': activity.starttime,
               'endtime': activity.endtime,
               'description': activity.description
               }
        returnData.append(buf)
    return HttpResponse(json.dumps(returnData, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")
        
def getJoinersByAct(request,aid):
    if 'user' not in request.session:
        return HttpResponse(status = 401)
    joiners = Joiner.objects.filter(aid = aid)
    returnData = []
    for joiner in joiners:
        user = joiner.user
        buf = {'uid': user.id,
               'username': user.username,
               'gender': user.gender
               }
        returnData.append(buf)
    return HttpResponse(json.dumps(returnData, ensure_ascii=False, cls=DjangoJSONEncoder), content_type="application/json")
