
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
from drawings.models import LottoTicket, Drawing, OfficialDrawing


def index(request):
    print "in index"
    return render(request, 'drawings/index.html')


def maintainDrawing(request, drawingId):
    print "in maintainDrawing"
    context = RequestContext(request, {'drawing': Drawing.objects.get(id=drawingId), 'ticketId': request.POST.get('ticketId')})
    return render(request, 'drawings/maintainDrawing.html', context)


def viewDrawings(request, ticketId):
    print "in viewDrawings"
    context = RequestContext(request, {'lotto_ticket': LottoTicket.objects.get(id=ticketId), 'official_drawings':OfficialDrawing.objects.all(), })
    return render(request, 'drawings/viewDrawings.html', context)


def viewTickets(request):
    print "in viewTickets"
    allTickets = LottoTicket.objects.all()
    context = {'latest_ticket_list': allTickets}
    return render(request, 'drawings/viewTickets.html', context)


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