import collections
from datetime import datetime, timedelta
from django.forms import ModelForm, forms
from drawings.models import Drawing, OfficialDrawing


class drawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['lotto_ticket', 'val1', 'val2', 'val3', 'val4', 'val5', 'mega_ball']


class viewDrawingsForm(forms.Form):
    def getApplicableOfficialDrawings(self, purchaseDate, numberOfDrawings):
        officialDrawings = []
        iterationDate = self.getNextDrawingDate(purchaseDate)
        drawingsRecorded = 0
        while iterationDate is not None and numberOfDrawings > drawingsRecorded:
            try:
                officialDrawings.append(OfficialDrawing.objects.get(drawing_date=iterationDate))
                iterationDate += timedelta(days=1)
                iterationDate = self.getNextDrawingDate(iterationDate)
                drawingsRecorded += 1
            except:
                return officialDrawings
        return officialDrawings

    # noinspection PyBroadException
    def getNextDrawingDate(self, iterationDate):
        while iterationDate <= datetime.date(OfficialDrawing.objects.latest('drawing_date').drawing_date):
            try:
                OfficialDrawing.objects.get(drawing_date=iterationDate)
                return iterationDate
            except:
                iterationDate = iterationDate+timedelta(days=1)
        return None

    def calculateWinningValue(self, numberCount, hitMegaBallInd):
        payout = 0
        if hitMegaBallInd:
            if numberCount == 0:
                payout = '1'
            if numberCount == 1:
                payout = '2'
            if numberCount == 2:
                payout = '5'
            if numberCount == 3:
                payout = '50'
            if numberCount == 4:
                payout = '5,000'
            if numberCount == 5:
                payout = 'JACKPOT'
        else:
            if numberCount == 3:
                payout = '5'
            if numberCount == 4:
                payout = '500'
            if numberCount == 5:
                payout = '1,000,000'
        return payout

    def calculateMatchedNumbers(self, ticketDrawings, officialDrawing):
        officalDrawingRegularNumbersList = [officialDrawing.val1, officialDrawing.val2, officialDrawing.val3, officialDrawing.val4, officialDrawing.val5]
        matchedNumbersDict = collections.OrderedDict()
        for ticketDrawing in ticketDrawings.all():
            regularNumbersMatched = 0
            megaBallMatched = False
            if ticketDrawing.val1 in officalDrawingRegularNumbersList:
                regularNumbersMatched += 1
            if ticketDrawing.val2 in officalDrawingRegularNumbersList:
                regularNumbersMatched += 1
            if ticketDrawing.val3 in officalDrawingRegularNumbersList:
                regularNumbersMatched += 1
            if ticketDrawing.val4 in officalDrawingRegularNumbersList:
                regularNumbersMatched += 1
            if ticketDrawing.val5 in officalDrawingRegularNumbersList:
                regularNumbersMatched += 1
            if ticketDrawing.mega_ball == officialDrawing.mega_ball:
                megaBallMatched = True
            if regularNumbersMatched or megaBallMatched:
                winningValue = self.calculateWinningValue(regularNumbersMatched, megaBallMatched)
                if winningValue:
                    matchedNumbersDict[ticketDrawing] = winningValue
        return matchedNumbersDict

    def generatePayoutDictionary(self, lottoTicket, applicableDrawings):
        payoutDict = collections.OrderedDict()
        for officialDrawing in applicableDrawings:
            matchedNumbersDict = self.calculateMatchedNumbers(lottoTicket.drawing_set, officialDrawing)
            payoutDict[officialDrawing.drawing_date] = matchedNumbersDict
        return payoutDict
