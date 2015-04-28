from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    
    # *** Homepage URL ***
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^thanks/$', 'contact.views.thanks', name='thanks'),
)
