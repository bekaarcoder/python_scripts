import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('template.html').read_text())
email = EmailMessage()
email['from'] = 'Shashank'
email['to'] = 'shashank.basant@gmail.com'
email['subject'] = 'Testing Python Email!'

email.set_content(html.substitute({'name': 'Shashank'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('howtowebtuts@gmail.com', 'merakutta007')
  smtp.send_message(email)
  print('Mail sent') 