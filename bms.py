import urllib2, sys
from bs4 import BeautifulSoup
import re
import smtplib
import time

site= "https://in.bookmyshow.com/buytickets/x-men-apocalypse-3d-hyderabad/movie-hyd-ET00029820-MT/" #Replace this your movieandcity url
date="20160525" #replace the date with the date for which you'd like to book tickets! Format: YYYYMMDD
site=site+date
hdr = {'User-Agent': 'Mozilla/5.0'}
venue ='CPCL' #this can be found by inspecting the element data-id for the venue where you would like to watch 
show='11:30 AM' #just replace it with your prefered show timing
delay=300 #timegap in seconds between 2 script runs 

TO = 'throwaway.aakarsh@gmail.com' #mail id for which you want to get alerted
GMAIL_USER = 'throwaway.aakarsh@gmail.com'
GMAIL_PASS = 'throw.@@karsh'
SUBJECT = 'Tickets are now available, Book fast'
TEXT = 'The tickets are now available for the ' + show + ' show at the venue ' +venue

def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
soup2=soup.find_all('div', {'data-online': 'Y'})
line = str(soup2)
soup3= BeautifulSoup(line)
soup4=soup3.find_all('a', {'data-venue-code': venue})
line1=str(soup4)
soup5=BeautifulSoup(line1)
soup6=soup3.find_all('a', {'data-display-showtime': show})
line2=str(soup6)
result=re.findall('data-availability="A"',line2)
if len(result)>0:
    print "Available"
    send_email()
else :
    print "Not available yet"
time.sleep(delay) 

