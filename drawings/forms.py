from django.forms import ModelForm, forms
from drawings.models import Drawing, OfficialDrawing
from datetime import datetime, timedelta


class drawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['lotto_ticket', 'val1', 'val2', 'val3', 'val4', 'val5', 'power_ball']


class viewDrawingsForm(forms.Form):
    def getApplicableOfficialDrawings(self, purchaseDate, numberOfDrawings):
        officialDrawings = []
        iterationDate = self.getNextDrawingDate(purchaseDate)
        drawingsRecorded = 0
        while iterationDate is not None or numberOfDrawings >= drawingsRecorded:
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
