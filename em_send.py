### Problem: Google Security: "To help keep your account secure, 
# starting May 30, 2022, ​​Google will no longer support the use of third-party apps 
# or devices which ask you to sign in to your 
# Google Account using only your username and password."

#Potential to utilise GMail API 

import smtplib
import ssl
from email.message import EmailMessage
from keys import PASWD

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "christophersamuelharris@gmail.com"
reciever_email = "christophersamuelharris@gmail.com"
password = PASWD

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context() #Need a secure connection when we connect to Gmail

#6/5/22 - Sending an email will fail (Timeout) as we cant turn less secure access ON 
print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string)
    
print("Success")