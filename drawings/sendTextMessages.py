import smtplib
import time
from time import strftime, localtime

username = 'millerry01@gmail.com'
password = '1otteryChecker'
fromaddr = 'millerry01@gmail.com'
toaddrs  = ['5172816829@vtext.com']

def get_Time() :
    return time.time()

def show_Full_Time() :
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def sendTexts(msg):
    print 'connecting...'
    server = smtplib.SMTP('smtp.gmail.com:587')
    print 'connected, starting ttls...'
    server.starttls()
    print 'ttls started, loging in...'
    server.login(username,password)
    print 'logged in, sending mail...'
    server.sendmail(fromaddr, toaddrs, msg)
    print 'mail sent'
    server.quit()