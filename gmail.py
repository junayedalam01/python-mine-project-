import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass # To securely input the password

# --- Email Configuration ---
sender_email = "send@gmail.com"
receiver_email = "rec@gmail.com" # Can be a list for multiple recipients
subject = "Hi ..."
body = "Every time I talk to you, my heart forgets all its worries. You’re my peace, my smile, my favorite thought."

# Prompt for the App Password securely
# It is recommended to use environment variables in production
# app_password = getpass.getpass(f"Enter your App Password for {sender_email}: ") 
# Or hardcode for simple testing (not recommended for production)
app_password = "app password in gmail" # Replace with your copied App Password

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Create a secure SSL context and connect to the server
# Use port 465 for SSL or 587 for starttls
smtp_server = "smtp.gmail.com"
port = 465  # For SSL

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context()) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication error: Check your email and App Password.")
except Exception as e:
    print(f"An error occurred: {e}")

