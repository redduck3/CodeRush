from django.conf.urls import patterns, include, url
from ourplatform import views

urlpatterns = patterns('',
#     url(r'^$', views.test, name='index'),
    url(r'^/post/activities/$', views.createActivities, name='createActivities'),
    url(r'^/get/activities/$'. views.getActivities, name='getActivities'),
    
    url(r'^/post/users/$'. views.createUser, name='createUser'),
    url(r'^/get/users/(?P<id>\d+)/$'. views.getUser, name='getUser'),
    url(r'^/put/users/$'. views.updateUser, name='updateUser'),
    url(r'^/delete/users/$'. views.deleteUser, name='deleteUser'),
    url(r'^/login/$'. views.login, name='login'),
    url(r'^/logout/$'. views.logout, name='logout'),
)
