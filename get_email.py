from ler_email import sender, subject
import re


# gets the adress information from the email
mail = re.search(r'<([^<>]+)>', sender)
endereco_email = mail.group(1)
sujeito = f'{subject}'

