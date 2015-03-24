from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
   
    # these URL patterns define the ajax calls to the backed for creating, updating, 
    # receiving, and deleting schedule entry items.
    url(r'^all/(?P<sched_id>\d+)/$', 'schedentry.views.all_entry', name='all_entry'),
    
    url(r'^add/$', 'schedentry.views.add_entry', name='add_entry'),
    url(r'^edit/$', 'schedentry.views.edit_entry', name='edit_entry'),
    url(r'^delete/$', 'schedentry.views.delete_entry', name='delete_entry'),
    
    
    
)
