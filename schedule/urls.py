from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
   
    url(r'^list/$', 'schedule.views.sched_list', name='sched_list'),
    
    url(r'^get/(?P<sched_id>\d+)/$', 'schedule.views.getSchedule'),
    url(r'^create/$', 'schedule.views.createSchedule'),
    
    # The edit URL in this case routes to show the actual calendar application
    # for that specific schedule
    url(r'^edit/(?P<sched_id>\d+)/$', 'schedule.views.editSchedule'),

    
)
