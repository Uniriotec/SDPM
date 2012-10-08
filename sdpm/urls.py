from django.conf.urls.defaults import patterns, include, url

from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       
     url(r'^admin/', include(admin.site.urls)),
)


#urlpatterns += patterns('django.contrib.auth.views',               
#
#    url(r'^login/$', 'login', {'template_name': 'user/login.html',}, name='login'),  
#    url(r'^logout/$', 'logout', {'template_name': 'user/login.html'},name='logout'),
#        
#
#)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    )
