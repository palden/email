import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'myself'
email['to'] = 'drikting@gmail.com'
email['subject'] = 'Create value for everyone'
email.set_content(html.substitute({'name': 'Tintin'}), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email_address_here@gmail.com', 'password_goes_here')
    smtp.send_message(email)
    print("all good")
