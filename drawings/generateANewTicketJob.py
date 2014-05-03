import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyLotto.settings")
from drawings.models import LottoTicket, Drawing

'''Comment out the lines you don't need'''

# CREATE A TICKET
ticket = LottoTicket()
ticket.ticket_title = raw_input('Ticket Name: ')
ticketTitle = ticket.ticket_title
ticket.date_purchased = raw_input('Date Purchased: ')  # eg '2014-04-01'
ticket.number_of_draws = int(raw_input('Number of Draws: '))
ticket.save()


#IMPORT DRAWINGS FOR A TICKET BASED OFF A CSV FILE
file = open('C:\Users\Milla\Desktop\May Drawings.txt')
fileText = file.read()
fileList = fileText.split('\n')
file.close()
LottoTicket.objects.get(id=1).drawing_set.all().delete()
draw = Drawing()
n = 1
for val in fileList:
    draw = Drawing()
    drawingList = val.split(',')
    draw.val1 = drawingList[0]
    draw.val2 = drawingList[1]
    draw.val3 = drawingList[2]
    draw.val4 = drawingList[3]
    draw.val5 = drawingList[4]
    draw.power_ball = drawingList[5]
    draw.lotto_ticket_id = 1
    draw.id = n
    n += 1
    draw.save()
for range in range(1,9):
    draw = Drawing()
    try:
        draw.lotto_ticket = LottoTicket.objects.get(ticket_title='May\'s Ticket')
        draw.val1 = raw_input('val1: ')
        draw.val2 = raw_input('val2: ')
        draw.val3 = raw_input('val3: ')
        draw.val4 = raw_input('val4: ')
        draw.val5 = raw_input('val5: ')
        draw.power_ball = raw_input('powerball: ')
    except:
        continue
    draw.save()