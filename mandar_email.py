import os
from dotenv import load_dotenv
import smtplib
import email
from get_email import endereco_email 

load_dotenv()

#gets the user and the receiver from the .env
usuario = os.getenv("EMAILER")
recebedor = os.getenv("RECEIVER")

def enviar_email(): 
    # set the message that will be sent on the email
    corpo_email = """Olá, muito obrigado por me contatar, caso seja pertinente,entrarei em contato em breve!"""
    msg = email.message.Message()
    # set the subject, from who it is and to who is it
    msg['Subject'] = "Assunto"
    msg['From'] = usuario
    msg['To'] = endereco_email
    # get the password from getenv
    senha = os.getenv("PASSWORD")
    msg.set_payload(corpo_email)

    # does le funny server thing
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    #logs in the server and sends the mail utilizing the utf-8 charset
    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
