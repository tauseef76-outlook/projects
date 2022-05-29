import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',25)
server.ehlo()       #function to start the server


with open("password.txt","r") as f:
    password = f.read()

server.login("anwartauseef37@gmail.com",password)

msg = MIMEMultipart()
msg["From"] = "test_mail"
msg["To"] = "anwartauseef37@gmail.com"
msg["subject"] = "This is a test mail."

with open(r"message.txt","r") as m:
    message = m.read()
    
msg.attach(MIMEText(message,"plain"))

 