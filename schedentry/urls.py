from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
   
    url(r'^employee/$', 'schedentry.views.employee', name='employee'),
    url(r'^manager/$', 'schedentry.views.manager', name='manager'),
    
)
