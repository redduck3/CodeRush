from django.conf.urls import patterns, include, url
from ourplatform import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/activities/$', views.createActivities, name='createActivities'),
    url(r'^get/activities/$', views.getActivities, name='getActivities'),
    url(r'^get/activities/undo$', views.getActivitiesUndo, name='getActivitiesUndo'),
    url(r'^get/activities/byid/(?P<id>\d+)$', views.getActivityById, name='getActivityById'),
    url(r'^get/activities/bykind/(?P<kid>\d+)$', views.getActivityByKind, name='getActivityByKind'),
    url(r'^get/activities/bykindundo/(?P<kid>\d+)$', views.getActivityByKindUndo, name='getActivityByKindUndo'),
    url(r'^put/activities/(?P<id>\d+)', views.updateActivity, name='updateActivity'),
    
    url(r'^post/users/$', views.createUser, name='createUser'),
    url(r'^get/users/(?P<id>\d+)/$', views.getUser, name='getUser'),
    url(r'^put/users/(?P<id>\d+)/$', views.updateUser, name='updateUser'),
    url(r'^delete/users/(?P<id>\d+)/$', views.deleteUser, name='deleteUser'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    
    url(r'^post/joiners/$', views.createJoiner, name='createJoiner'),
    url(r'^get/joiners/byuser/(?P<uid>\d+)/$', views.getJoinersByUser, name='getJoinerByUser'),
    url(r'^get/joiners/byact/(?P<aid>\d+)/$', views.getJoinersByAct, name='getJoinerByAct'),
    url(r'^delete/joins/(?P<aid>\d+)/$', views.deleteJoiner, name='deleteJoiner'),
)
