from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url('', include('drawings.urls', namespace='drawings')),
    url(r'^/maintainDrawing/(?P<drawingId>\d+).+', include('drawings.urls', namespace='drawings')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^submit/', include('drawings.urls', namespace='drawings')),
)
