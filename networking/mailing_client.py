# This is by default password

# from email.mime import text
# import smtplib
# from email import encoders
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.ehlo()       #function to start the server
# server.starttls()


# with open("projects/networking/password.txt","r") as f:
#     password = f.read()

# server.login("anwartauseef37@gmail.com",password)

# msg = MIMEMultipart()
# msg["From"] = "test_mail"
# msg["To"] = "1993taz@gmail.com"
# msg["subject"] = "This is a test mail."

# with open(r"projects/networking/message.txt","r") as m:
#     message = m.read()

# msg.attach(MIMEText(message,"plain"))

# filename = "projects/networking/image.jpeg"
# attachment = open(filename,"rb")

# p = MIMEBase("application","octet-stream")
# p.set_payload(attachment.read())

# encoders.encode_base64(p)
# p.add_header("Content-Disposition",f'attachment;filename={filename}')

# msg.attach(p)

# text = msg.as_string()
# server.sendmail("anwartauseef37@gmail.com","1993taz@gmail.com",text)

# server.quit()
#
# =======================================================================

# This program is using app code

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# TODO: replace with your email address
sender_email = "anwartauseef37@gmail.com"
# TODO: replace with your recipients
receiver_email = ["tauseef76@outlook.com", "1993taz@gmail.com"]
password = 'mpjsujrmpqydajwi'  # TODO: replace with your 16-digit-character password

# assuming these two values are from your analysis
score = 0.86
today_date = '2021-08-08'

# initialise message instance
msg = MIMEMultipart()
msg["Subject"] = "Training Job Notification on {}".format(today_date)
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email)

# Plain text
text = """\
This line is to demonstrate sending plain text."""

body_text = MIMEText(text, 'plain')  #
msg.attach(body_text)  # attaching the text body into msg

html = """\
<html>
  <body>
    <p>Hi,<br>
    <br>
    This is to inform the training job has been completed. The AUC for the job on {} is {} <br>
    Thank you. <br>
    </p>
  </body>
</html>
"""

body_html = MIMEText(html.format(today_date, score),
                     'html')  # parse values into html text
msg.attach(body_html)  # attaching the text body into msg

# Image
# TODO: replace your image filepath/name
img_name = 'projects/networking/image.jpeg'
with open(img_name, 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename=img_name)
    msg.attach(img)

## Attachments in general
# Replace filename to your attachments. Tested and works for png, jpeg, txt, pptx, csv
# TODO: replace your attachment filepath/name
filename = 'projects/networking/message.txt'
with open(filename, 'rb') as fp:
    attachment = MIMEApplication(fp.read())
    attachment.add_header('Content-Disposition',
                          'attachment', filename=filename)
    msg.attach(attachment)

context = ssl.create_default_context()
# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # check connection
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # check connection
    server.login(sender_email, password)

    # Send email here
    server.sendmail(sender_email, receiver_email, msg.as_string())

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
