#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "saidatkasymova@gmail.com"        # replace with your email
sender_password = "vhizwjpvamantemp"         # use a Gmail App Password, not your real password
receiver_email = "saidatkasymova@gmail.com"     # replace with the recipient

subject = "Cron Job Notification"
body = f"This is an automated message. Script ran successfully at {datetime.now()}."

message = MIMEText(body)
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
