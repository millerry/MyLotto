import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyLotto.settings")
import urllib2
import json
from HTMLParser import HTMLParser
from datetime import datetime
from drawings.models import OfficialDrawing, LottoTicket, Drawing


class parseHtml(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print "Encountered a start tag:", tag
        pass

    def handle_endtag(self, tag):
        # print "Encountered an end tag :", tag
        pass

    def handle_data(self, data):
        index = 0
        for item in data:
            constructOfficialDrawing(item)


# noinspection PyBroadException
def constructOfficialDrawing(data):
    date_object = datetime.strptime(data['draw_date'], '%Y-%m-%dT%H:%M:%S')
    date_object = date_object.date()
    megaball = data['mega_ball']
    multiplier = ""
    try:
        multiplier = data['multiplier']
    except:
        pass
    winning_numbers_list = data['winning_numbers'].split()
    try:
        OfficialDrawing.objects.get(drawing_date=str(date_object))
    except:
        newDrawing = OfficialDrawing(drawing_date=date_object)
        newDrawing.val1 = winning_numbers_list[0]
        newDrawing.val2 = winning_numbers_list[1]
        newDrawing.val3 = winning_numbers_list[2]
        newDrawing.val4 = winning_numbers_list[3]
        newDrawing.val5 = winning_numbers_list[4]
        newDrawing.power_ball = megaball
        if multiplier:
            newDrawing.multiplier = multiplier
        else:
            newDrawing.multiplier = 1
        newDrawing.save()
        print 'inserted an official drawing in the database \n'


base_url = urllib2.urlopen('http://data.ny.gov/resource/5xaw-6ayf.json')
html = base_url.read()
json_data = json.loads(html)
data_handler = parseHtml()
data_handler.handle_data(json.loads(html))

print OfficialDrawing.objects.get(drawing_date='2014-04-15').multiplier

# script for creating a ticket and entering one drawing on it
# ticket = LottoTicket()
# ticket.ticket_title = 'April Ticket'
# ticket.date_purchased = '2014-04-01'
# ticket.number_of_draws = 9
# ticket.save()
# draw = Drawing()
# draw.lotto_ticket = LottoTicket.objects.get(ticket_title='April Ticket')
# draw.val1 = 03
# draw.val2 = 21
# draw.val3 = 30
# draw.val4 = 31
# draw.val5 = 51
# draw.power_ball = 02
#
# draw.save()

