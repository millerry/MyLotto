import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyLotto.settings")
import urllib2
import json
from forms import viewDrawingsForm
from HTMLParser import HTMLParser
from datetime import datetime
from drawings.models import OfficialDrawing, LottoTicket, Drawing
from drawings import sendTextMessages


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


def createSMSListFromFile(fileName):
    fileObject = open(fileName, 'rU')
    fileText = fileObject.read()
    fileObject.close()
    return fileText.split(',')

totalOfficialDrawings = len(OfficialDrawing.objects.all())
base_url = urllib2.urlopen('http://data.ny.gov/resource/5xaw-6ayf.json')
html = base_url.read()
json_data = json.loads(html)
data_handler = parseHtml()
data_handler.handle_data(json.loads(html))

# @comment if an entry was added, send out an SMS alert
if len(OfficialDrawing.objects.all()) > totalOfficialDrawings:
    lottoTicket = LottoTicket.objects.get(ticket_title="May\'s Ticket")
    drawingsForm = viewDrawingsForm()
    payoutDict = drawingsForm.generatePayoutDictionary(lottoTicket, viewDrawingsForm.getApplicableOfficialDrawings(drawingsForm,lottoTicket.date_purchased, lottoTicket.number_of_draws))

    total = 0
    msg = "Lotto Update"
    shortMsg = msg
    lastAmount = ""
    lastDateString = ""
    numberOfDrawsLeft = lottoTicket.number_of_draws - len(payoutDict.keys())
    for key, value in payoutDict.items():
        lastAmount = 0
        for k,v in value.items():
            lastDateString = str(key.month) + '/' + str(key.day)
            if v:
               lastAmount += int(v)
               drawing = Drawing.objects.get(id=k.id)
               msg += '\n' + lastDateString
               msg += ' ' + str(drawing.val1) \
                      + ' ' + str(drawing.val2) \
                      + ' ' + str(drawing.val3) \
                      + ' ' + str(drawing.val4) \
                      + ' ' + str(drawing.val5) \
                      + ' ' + str(drawing.power_ball)
               msg += ': $' + v
               total += int(v)

    totalString = '\nTo-Date: $' + str(total)
    msg += totalString
    shortMsg += '\nLast Draw - ' + lastDateString + ': $' + str(lastAmount) + totalString + '\nDraws remaining: ' + str(numberOfDrawsLeft)
    toaddrs_shortMessage = createSMSListFromFile('shortMessageUsers.txt')
    toaddrs_longMessage = createSMSListFromFile('longMessageUsers.txt')

    sendTextMessages.sendTexts(shortMsg, toaddrs_shortMessage)
    sendTextMessages.sendTexts(shortMsg, toaddrs_longMessage)
