import os
from dotenv import load_dotenv
import smtplib
import email
from main import sujeito 

load_dotenv()

usuario = os.getenv("EMAILER")
recebedor = os.getenv("RECEIVER")

def enviar_email():  
    corpo_email = sujeito
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = usuario
    msg['To'] = recebedor
    senha = os.getenv("PASSWORD")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()


