import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- SMTP config ---
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "saidatkasymova@gmail.com"  
sender_password = ""   # removed before committing    
receiver_email = "saidatkasymova@gmail.com"   # 

subject = "Action Required: Verify Your Debit Card"

# Link to your fake page
phish_link = "http://localhost:8080/index.html"

body = f"""
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Bank Notice</title></head>
<body style="font-family: Arial, sans-serif; background:#f2f4f7; margin:0; padding:20px;">
  <div style="max-width:600px; margin:0 auto; background:#fff; padding:30px; border-radius:10px;">

    <h2 style="color:#1a1a1a;">Important: Card Verification Required</h2>

    <p style="color:#333; font-size:14px;">Dear Customer,</p>
    <p style="color:#333; font-size:14px;">
      We detected unusual activity on your debit card. For your protection,
      your card has been temporarily limited until you verify your details.
    </p>
    <p style="color:#333; font-size:14px;">
      Please click the button below to complete a quick verification:
    </p>

    <p style="text-align:center; margin:30px 0;">
      <a href="{phish_link}"
         style="background:#1877f2; color:#fff; padding:12px 24px;
                text-decoration:none; border-radius:6px; font-weight:bold;">
        Verify My Card Now
      </a>
    </p>

    <p style="color:#666; font-size:12px;">
      If you did not request this, you can safely ignore this message.
    </p>
    <p style="color:#999; font-size:11px;">
      Secure Card Services, 1601 Willow Road, Menlo Park, CA 94025
    </p>
  </div>
</body>
</html>
"""

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "html"))

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
