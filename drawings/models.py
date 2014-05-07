from django.db import models


class LottoTicket(models.Model):
    ticket_title = models.CharField(max_length=50)
    date_purchased = models.DateField('Data Purchased')
    number_of_draws = models.IntegerField('Number of Draws')
    multiplier_ind = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.date_purchased)


class Drawing(models.Model):
    lotto_ticket = models.ForeignKey(LottoTicket)
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()
    val4 = models.IntegerField()
    val5 = models.IntegerField()
    mega_ball = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id)


class OfficialDrawing(models.Model):
    drawing_date = models.DateTimeField('Drawing Date', primary_key=True)
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()
    val4 = models.IntegerField()
    val5 = models.IntegerField()
    mega_ball = models.IntegerField()
    multiplier = models.IntegerField()

    def __unicode__(self):
        return unicode(self.drawing_date)