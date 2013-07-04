from django.conf.urls import patterns, include, url
from django.conf import settings

from im.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'texxt.views.home', name='home'),
    # url(r'^texxt/', include('texxt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login_view),
    url(r'^accounts/logout/$', logout_view),
    url(r'^accounts/profile/$', profile_view),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^$', lists),
    url(r'^lists/', lists),
    url(r'^upload/', upload),
    url(r'^uploadfile/', upload_file),
    url(r'^generate_csv/', generate_csv),

)