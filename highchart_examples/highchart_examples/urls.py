from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # the basic home page
    url(r'^$', 'line_charts.views.home', name='home'),
    url(r'^base_line/$', 'line_charts.views.base_line', name='base_line'),


    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)

    urlpatterns+=static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
