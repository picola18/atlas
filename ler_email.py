import imaplib
import email
from dotenv import load_dotenv
import os

load_dotenv()

# get the user and the password from the .env file
usuario = os.getenv("EMAILER")
password = os.getenv("PASSWORD")

# do the imap connection
imap_host = 'imap.gmail.com'
imap_user = usuario
imap_pass = password

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

# login to server
imap.login(imap_user, imap_pass)

# start the function
def ler_email():
    with imaplib.IMAP4_SSL(imap_host) as imap:
      imap.login(imap_user, imap_pass)
# select the place where we do the funny reading
imap.select('inbox')
_, data = imap.search(None, 'ALL')
latest_email_id = data[0].split()[-1]
# i have absolutely 0 idea what this does lmao
_, message_data = imap.fetch(latest_email_id, '(BODY.PEEK[HEADER])')
message = email.message_from_bytes(message_data[0][1])
# subject gets the subject from the email and sender gets from who the msg is
subject = message['Subject']
sender = message['From']
# prints the results
print(f'Subject: {subject}')
print(f'Sender: {sender}')
ler_email()