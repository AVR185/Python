from fileinput import filename
import requests # http requests
from bs4 import BeautifulSoup # Web scrapping
import smtplib # Send email
from email.message import EmailMessage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText # Email body
import datetime # System time and date manipulation

# Variables
now = datetime.datetime.now()
content = '' # Email content placeholder

# Extracting Hacker News Stories
def extract_news(url):
    print('Extracting Hacker News Stories...')
    htmlText = '<b>HN Top Stories:</b>\n<br>' + '-' * 50 +'<br>'
    response = requests.get(url)
    content = response.content # Content of the web page
    soup = BeautifulSoup(content, 'html.parser')

    for i,tag in enumerate( soup.find_all('td', attrs={'class': 'title', 'valign': ''}) ): # Extract titles # td class=titlle and without valign attribute
        htmlText += (str(i+1) + ' :: ' + tag.text + "\n" + '<br>' ) if tag.text != 'More' else '' # Save text, except the last row, line 'more'

    return htmlText


content += extract_news('https://news.ycombinator.com/')
content += '<br>----------<br>'
content += '<br><br>End of Message'


# Lets send the email
print('Composing Email...')

"""
# ------- OUTDATE ------ NOWADAYS This code doesn't work
# Emails Settings
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'avr_heavy_metal@hotmail.com'
PASS = '*********'
TO = '************

#fp = open(file_name, 'rb')
# Create a text/plain message
#msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email] ' +str(now.day)+ '-' +str(now.month)+ '-' +str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html')) # Add html content
# fp.close()

# Init Server
print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1) # get error messages
server.ehlo()
server.starttls() # enable security
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
"""

# Email with outlook -> The windows application must be configured
import win32com.client as win32

olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

# construct email item object
mailItem = olApp.CreateItem(0) # 0 -> Mail item
mailItem.Subject = 'Top News Stories HN [Automated Email] ' +str(now.day)+ '-' +str(now.month)+ '-' +str(now.year)

# mailItem.BodyFormat = 1 # 1 -> Plain text // 2 -> HTML // 3 -> Rich text // 0 -> Undefined
# mailItem.Body = 'Hello There'
mailItem.BodyFormat = 2
mailItem.HTMLBody = content

mailItem.To = 'avr.evergrey@gmail.com' 
mailItem.Sensitivity  = 2
# optional (account you want to use to send the email)
mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('avr_heavy_metal@hotmail.com')))

# Different options
# mailItem.Display()
# mailItem.Save()
mailItem.Send()

print('Email Sent...')