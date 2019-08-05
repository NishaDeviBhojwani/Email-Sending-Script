# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:41:38 2019

@author: Nisha Bhojwani
"""

import csv
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# Mail Body content 
mailBody = ''' Mail Body Content 
'''

#The mail addresses and password
senderAddress = 'Your_Email@gmail.com'
senderPassword = 'YOUR PASSWORD'

EmailsFile = open('emails_File.csv')             #Receipents emails file 
emailsCSV = csv.reader(EmailsFile)
receiverEmails = []                         #List for Receipents email
next(emailsCSV)                             # Skip header row

for email in emailsCSV:                     # emails from csv to list 
  receiverEmails.append(email)
  
  
for i in  range(len(receiverEmails)):
    message = MIMEMultipart()                       # setups Email 
    message['From'] = 'YOUR_EMAIL@gmail.com'
    message['To'] = ', '.join(receiverEmails[i])    # join used for to mail multiple receipents
    message['Subject'] = 'Email SUBJECT '
    message.attach(MIMEText(mailBody, 'plain'))
    attachmentFileName = 'Attachment.pdf'          # Attachment file
    fileName = "AttachmentName.pdf"
    attach_file = open(attachmentFileName, 'rb')    # Open the file as binary mode
    payload = MIMEBase('application', 'pdf')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)                 #encode the attachment
    payload.add_header('Content-Disposition',"attachment; filename= "+fileName)
    message.attach(payload)
    session = smtplib.SMTP('smtp.gmail.com', 587)   #use gmail with port
    session.starttls()                              #enable security
    session.login(senderAddress, senderPassword)    #login with mail_id and password
    text = message.as_string()
    session.sendmail(senderAddress, receiverEmails[i], text)
    session.quit()
    message = ""
    print('Mail Sent')

