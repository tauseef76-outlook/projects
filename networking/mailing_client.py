import smtplib

server = smtplib.SMTP('smtp.gmail.com',25)
server.ehlo()       #function to start the server
