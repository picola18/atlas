from ler_email import sender, subject
import re



mail = re.search(r'<([^<>]+)>', sender)
endereco_email = mail.group(1)
sujeito = f'{subject}'


