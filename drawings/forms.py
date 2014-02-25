from django.forms import ModelForm
from drawings.models import Drawing


class drawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['lotto_ticket', 'drawing_date', 'val1', 'val2', 'val3', 'val4', 'val5', 'power_ball']

