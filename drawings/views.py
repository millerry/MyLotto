
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
from drawings.models import LottoTicket, Drawing


def index(request):
    print "in index"
    return render(request, 'drawings/index.html')


def maintainDrawing(request, drawingId):
    print "in maintainDrawing"
    context = RequestContext(request, {'drawing':Drawing.objects.get(id=drawingId), })
    return render(request, 'drawings/maintainDrawing.html', context)


def viewDrawings(request):
    print "in viewDrawings"
    latest_drawing_list = Drawing.objects.all()
    context = {'latest_drawing_list': latest_drawing_list}
    return render(request, 'drawings/viewDrawings.html', context)


def addDrawing(request): #, number2, number3, number4, number5, powerball):
    print "in addDrawing"
    drawing = Drawing(drawing_date=timezone.now())
    drawing.val1 = 11
    drawing.val2 = 22
    drawing.val3 = 33
    drawing.val4 = 44
    drawing.val5 = 55
    drawing.power_ball = 66
    drawing.save()
    return index(request)