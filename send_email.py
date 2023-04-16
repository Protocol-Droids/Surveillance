import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import ssl

def send_mail(message='This is a test email.', recipient_email='martin.arthur.andersen@gmail.com', subject='Email from bot'):
    sender_email = 'bot@nettking.no'
    sender_name = 'Nettking Surveillance Bot'
    msg = MIMEText(message)
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # create an SSL/TLS secure connection to the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.proisp.no', 465, context=context) as smtp:
        smtp.login(sender_email, 'JabbaJabbaHei1990')
        smtp.sendmail(sender_email, recipient_email, msg.as_string())
