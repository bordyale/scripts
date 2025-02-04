import os
import re
import datetime
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Change to your own account information
to = 'alessio.bordignon@gmail.com'
gmail_user = 'system.bordignon@gmail.com'
gmail_password = 'dwqq fpef txem bgun'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
files = os.listdir('/home/ale/Dropbox/backupMySql/pi')


today = datetime.date.today()
today_date = today.strftime("%Y-%m-%d")


files_in_range = []
bck_result=''
for fl in files:
    if bool(re.search(today_date,fl)):
        files_in_range.append(fl)

if len(files_in_range)==3:
    bck_result='OK'
else:
    bck_result='NO'




msg = MIMEText('BACKUP SUCCESS CHECK')
msg['Subject'] = f'{bck_result} bck on VF Ofbiz PI4'
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
