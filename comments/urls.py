from django.conf.urls import patterns, include, url
from django.contrib import admin

# These patterns generate how the URL structure of the overall site will work.  
# All URL's route through this particular page, always.  
# This particular page acts as a controller for the rest of the URL's, 
# sending each request to the correct app

urlpatterns = patterns('',
    
    url(r'^add/$', 'comments.views.addComment'),
    
    #url(r'^about/$', 'hourly.views.about', name='about'),

)