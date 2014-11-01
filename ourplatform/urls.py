from django.conf.urls import patterns, include, url
from ourplatform import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/activities/$', views.createActivities, name='createActivities'),
    url(r'^get/activities/$', views.getActivities, name='getActivities'),
    url(r'^get/activities/undo$', views.getActivitiesUndo, name='getActivitiesUndo'),
    url(r'^get/activities/(?P<id>\d+)$', views.getActivityById, name='getActivityById'),
    url(r'^put/activities/(?P<id>\d+)', views.updateActivity, name='updateActivity'),
    
    url(r'^post/users/$', views.createUser, name='createUser'),
    url(r'^get/users/(?P<id>\d+)/$', views.getUser, name='getUser'),
    url(r'^put/users/(?P<id>\d+)/$', views.updateUser, name='updateUser'),
    url(r'^delete/users/(?P<id>\d+)/$', views.deleteUser, name='deleteUser'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
)
