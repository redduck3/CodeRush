from django.conf.urls import patterns, include, url
from ourplatform import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='index'),
)
