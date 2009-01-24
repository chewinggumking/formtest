from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'index.html'}),
	(r'^show/$', 'formtest.tester.views.showing'),
	(r'^clients/$', 'formtest.tester.views.client_list'),
	(r'^admin/(.*)', admin.site.root),

)
