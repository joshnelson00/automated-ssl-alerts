from dotenv import load_dotenv # type: ignore
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

# Email details
sender = os.getenv("SENDER_EMAIL")
recipient = os.getenv("RECIPIENT_EMAIL")
subject = "Hello World Subject Line!"
message_body = "THIS IS A TEST MESSAGE"

# Create the email
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject
msg.attach(MIMEText(message_body, 'plain'))

# Get password from environment variable
password = os.getenv("APP_PASSWORD")

if not password:
    raise ValueError("APP_PASSWORD not set in environment variables")

# Send the email
with smtplib.SMTP("smtp.mail.me.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.send_message(msg)
    