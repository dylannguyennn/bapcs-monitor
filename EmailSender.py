import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from RedditBot import *

class EmailSender:
    SERVER_ADDRESS = 'smtp.gmail.com'
    TLS_PORT = 587

    def __init__(self, sender_address, sender_password, recipient_address):
        self.sender_address = sender_address
        self.sender_password = sender_password
        self.recipient_address = recipient_address
        self.server = None

    def start_server(self):
        self.server = smtplib.SMTP(self.SERVER_ADDRESS, self.TLS_PORT)
        self.server.starttls()
        self.server.login(self.sender_address, self.sender_password)

    def send_email(self, title, url, score):
        self.start_server()

        message = MIMEMultipart()
        message['From'] = self.sender_address
        message['To'] = self.recipient_address
        message['Subject'] = f"Top BAPCS Deals ({date.today():%Y-%m-%d})"

        # Message formatting
        body = ""

        for i in range(len(title)):
            body += f"{title[i]}\n"
            body += f"{url[i]}\n"
            body += f"{score[i]} upvotes\n"
            body += "\n"

        body = MIMEText(body)
        message.attach(body)

        message = message.as_string()

        self.server.sendmail(self.sender_address, self.recipient_address, message)
        self.server.quit()
