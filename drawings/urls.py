from django.conf.urls import patterns, url
from drawings import views

urlpatterns = patterns(
    '',

    url(r'^$', views.index, name='index'),

    url(r'^viewTickets/viewDrawings/(?P<ticketId>\d+)$', views.viewDrawings, name='viewDrawings'),

    url(r'^.+viewDrawings/(?P<ticketId>\d+)$', views.viewDrawings, name='viewDrawings'),

    url(r'^viewTickets/$', views.viewTickets, name='viewTickets'),

    url(r'^.+maintainDrawing/(?P<drawingId>\d+)$', views.maintainDrawing, name='maintainDrawing'),

    url(r'^submit/$', views.addDrawing, name='addDrawing')
)