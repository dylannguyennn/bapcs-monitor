from dotenv import load_dotenv
from RedditBot import *
from EmailSender import *
import datetime
import os

load_dotenv()

bot = RedditBot('bot1', 'BuildAPCSales')
bot.connect()
title, url, score = bot.fetch_submissions()

sender_address = os.getenv('SENDER_ADDRESS')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_address = os.getenv('RECIPIENT_ADDRESS')

email = EmailSender(sender_address, sender_password, recipient_address)
email.send_email(title, url, score)


