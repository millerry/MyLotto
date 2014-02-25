from django.conf.urls import patterns, url
from drawings import views

urlpatterns = patterns(
    '',

    url(r'^$', views.index, name='index'),

    url(r'^viewDrawings/$', views.viewDrawings, name='viewDrawings'),

    url(r'^.+maintainDrawing/(?P<drawingId>\d+)$', views.maintainDrawing, name='maintainDrawing'),

    url(r'^submit/$', views.addDrawing, name='addDrawing')
)