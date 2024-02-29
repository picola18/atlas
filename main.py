from ler_email import sender, subject
import re



mail = re.search(r'<([^<>]+)>', sender)
endereco_email = mail.group(1)
sujeito = f'{subject}'


sys_msg = "you are a useful assistent, gather the bits of info you can find in the message and answer it in a professional, thankful, manner, either in portuguese or in english, depending on the user message."


