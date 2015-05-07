from django.conf.urls import patterns, include, url
from django.contrib import admin

# These patterns generate how the URL structure of the overall site will work.  
# All URL's route through this particular page, always.  
# This particular page acts as a controller for the rest of the URL's, 
# sending each request to the correct app

urlpatterns = patterns('',
                       
    (r'^profile/', include('userprofile.urls')),
    (r'^sched/', include('schedule.urls')),
    (r'^entry/', include('schedentry.urls')),
    (r'^comment/', include('comments.urls')),
    
    # *** Homepage URL ***
    url(r'^$', 'hourly.views.home', name='home'),
    url(r'^about/$', 'hourly.views.about', name='about'),
    #url(r'^services/$', 'hourly.views.services', name='services'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^thanks/$', 'contact.views.thanks', name='thanks'),
    
    url(r'^signin/$', 'hourly.views.signin', name='signin'),
    url(r'^signup/$', 'hourly.views.signup', name='signup'),

    url(r'^dash/$', 'hourly.views.dashboard', name='dashboard'),
    url(r'^employees/$', 'hourly.views.employee_list', name='employee_list'),

    # *** Admin site URL ***
    # This enables the django admin site and it's in-browser features.  
    # It allows full CRUD access to the database 
    url(r'^admin/', include(admin.site.urls)),
    
    # *** User Authorization URL patterns ***
    # this includes the browser-side parsing of the login data (/auth),
    # the logout request (/request),
    # the successful login redirect (/success), 
    # and the page reached if invalid login information is sent (/invalid).
    url(r'^user/auth/$', 'hourly.views.auth_view'),
    url(r'^user/logout/$', 'hourly.views.logout'),
    url(r'^user/success/$', 'hourly.views.success'),
    url(r'^user/invalid/$', 'hourly.views.invalid_login'),
    url(r'^user/register/$', 'hourly.views.register_user'),
    url(r'^user/register_success/$', 'hourly.views.register_success'),
    
    
)
