from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from djangofett import settings
from portal.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangofett.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fettdb/', include('fettdb.urls')),
    url(r'^userctrl/', include('portal.urls')),
    url(r'^djangofett/', include('portal.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
