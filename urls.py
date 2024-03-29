from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from demo.prpv.views import searchObservations, testTable, testTable2, consultation, addObservation, testAutocomplete

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^selectable/', include('selectable.urls')),
    url(r'^search/', searchObservations),
    url(r'^consultation/', consultation),
    url(r'^observations/', addObservation),
    url(r'^autocomplete/', testAutocomplete),    
    url(r'^test/', testTable),
    url(r'^test2/', testTable2),
)
urlpatterns += staticfiles_urlpatterns()
