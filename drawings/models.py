import datetime
import calendar

from django.db import models
from django.utils import timezone


class LottoTicket(models.Model):
    ticket_title = models.CharField(max_length=50)
    date_purchased = models.DateField('Data Purchased')
    number_of_draws = models.IntegerField('Number of Draws')

    # def draw_dates(self):
    #     draw_dates = []
    #     first_draw = calendar.Calendar
    #     return timezone.datetime.day >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return unicode(self.date_purchased)


class Drawing(models.Model):
    lotto_ticket = models.ForeignKey(LottoTicket)
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()
    val4 = models.IntegerField()
    val5 = models.IntegerField()
    power_ball = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id)
