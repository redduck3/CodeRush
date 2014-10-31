from django.conf.urls import patterns, include, url
from ourplatform import views

urlpatterns = patterns('',
#     url(r'^$', views.test, name='index'),
    url(r'^/post/activities/$', views.createActivities, name='createActivities'),
    url(r'^/get/activities/$'. views.getActivities, name='getActivities'),
)
