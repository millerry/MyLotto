import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyLotto.settings")
from drawings.models import LottoTicket, Drawing

'''This is the quick and dirty way to store some data about a new ticket'''
# todo: Move this functionality to a web page instead of a command prompt

# Create a ticket and populate its values based off command prompts
ticket = LottoTicket()
ticket.ticket_title = raw_input('Ticket Name: ')
ticketTitle = ticket.ticket_title
ticket.date_purchased = raw_input('Date Purchased (YYYY-MM-DD): ')  # eg '2014-04-01'
ticket.number_of_draws = int(raw_input('Number of Draws: '))
ticket.save()

# Import drawings for a ticket from a csv file
file = open('C:\Users\Milla\Desktop\May Drawings.txt')
fileText = file.read()
numberSets = fileText.split('\n')
file.close()
LottoTicket.objects.get(id=1).drawing_set.all().delete()
draw = Drawing()
n = 1
for item in numberSets:
    draw = Drawing()
    drawingList = item.split(',')
    draw.val1 = drawingList[0]
    draw.val2 = drawingList[1]
    draw.val3 = drawingList[2]
    draw.val4 = drawingList[3]
    draw.val5 = drawingList[4]
    draw.mega_ball = drawingList[5]
    draw.lotto_ticket_id = 1
    draw.id = n
    n += 1
    draw.save()