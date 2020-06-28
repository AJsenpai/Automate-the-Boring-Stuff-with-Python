# textMyself.py - Defines the textmyself() function that texts a message passed to it as a string.

# Preset values:
account_sid = "AC133eba3e1c1b425cdbac3ce94a6a3934"
auth_token = "ea96abd7bb0319fb81028bf9135320d4"
myNumber = "+917976101244"
twilioNumber = "+14693522494"
from twilio.rest import Client


def textMyself(message):
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=twilioNumber, to=myNumber)


"""
# Whenever you want one of your programs to text you, just add the following:
import textmyself
textmyself.textmyself('The boring task is finished.')
"""
